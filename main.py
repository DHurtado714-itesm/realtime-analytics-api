from fastapi import FastAPI
from views import router

app = FastAPI()


app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, poart=8000)
