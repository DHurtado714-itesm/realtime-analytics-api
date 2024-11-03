from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models import PageView
from databse import db
from config import redis_client

router = APIRouter()


class TrackRequest(BaseModel):
    page_id: str
    user_id: str


@router.post("/track")
async def track_page_view(request: TrackRequest):
    try:
        page = await db.pageviews.find_one({"page_id": request.page_id})

        if page:
            if request.user_id not in page["unique_visitors"]:
                page["unique_visitors"].append(request.user_id)
            page["views"] += 1
            await db.pageviews.update_one({"page_id": request.page_id}, {"$set": page})
        else:
            page = PageView(
                page_id=request.page_id, unique_visitors=[request.user_id], views=1
            )
            await db.pageviews.insert_one(page.dict())

        redis_client.delete("stats")
        return {"message": "Page view tracked successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stats")
async def get_stats():
    cached_stats = redis_client.get("stats")

    if cached_stats:
        return eval(cached_stats)

    try:
        stats = await db.pageviews.find().to_list(100)
        for stat in stats:
            stat["_id"] = str(stat["_id"])

        redis_client.setex("stats", 60, str(stats))
        return stats

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
