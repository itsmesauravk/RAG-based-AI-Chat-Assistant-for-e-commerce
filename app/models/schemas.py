from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    session_id: str = None

class ChatResponse(BaseModel):
    response: str
    confidence: float = None
    sources: list = []