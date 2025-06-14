from pydantic import BaseModel
from typing import List, Dict, Optional


class Card(BaseModel):
    user_id: int
    items: List[int]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
