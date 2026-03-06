
from pydantic import BaseModel

class ChatbotRequest(BaseModel):
    message: str

class ChatbotResponse(BaseModel):
    response: str

# You can access pydantic version like this:
# print(pydantic.VERSION)