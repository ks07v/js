from pydantic import BaseModel
from typing import List, Optional


class ChatRequest(BaseModel):
    user_id: str
    message: str


class ChatResponse(BaseModel):
    answer: str
    source: List[str]
    intent: str
    resp_type: str


class Feedback(BaseModel):
    chat_id: str
    rating: int
    comment: Optional[str] = None


class Subscription(BaseModel):
    product_id: str
    name: str
    pay_cycle: str
    pay_amt: int
