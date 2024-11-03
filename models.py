from pydantic import BaseModel, Field
from typing import List


class PageView(BaseModel):
    page_id: str
    views: int = 0
    unique_visitors: List[str] = Field(default_factory=list)
