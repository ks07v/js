from fastapi import FastAPI, HTTPException
from typing import List

from .schemas import ChatRequest, ChatResponse, Feedback, Subscription

app = FastAPI(title="Smart-SubMate")

# Example in-memory data stores
subscriptions_db = {
    "user1": [
        Subscription(product_id="netflix", name="Netflix", pay_cycle="monthly", pay_amt=15000)
    ]
}
feedback_store: List[Feedback] = []


@app.post("/v1/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest) -> ChatResponse:
    # Very naive intent detection
    intent = "SUB_CANCEL" if "해지" in req.message else "GENERAL"
    if intent == "SUB_CANCEL":
        answer = "해지 안내입니다."
    else:
        answer = "안녕하세요! 무엇을 도와드릴까요?"
    return ChatResponse(answer=answer, source=[], intent=intent, resp_type="rule")


@app.get("/v1/subscription/{user_id}")
def get_subscription(user_id: str):
    subs = subscriptions_db.get(user_id)
    if subs is None:
        raise HTTPException(status_code=404, detail="user not found")
    return subs


@app.post("/v1/feedback")
def feedback_endpoint(feed: Feedback):
    feedback_store.append(feed)
    return {"status": "ok"}
