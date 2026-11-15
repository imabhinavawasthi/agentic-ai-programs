# status (False, True), output, tokens, email_id
from pydantic import BaseModel, EmailStr, PositiveInt

class GeminiResponse(BaseModel):
    output: str
    tokens: PositiveInt
    email_id: EmailStr
    status: bool


res1 = GeminiResponse(
    output="Hello, how are you",
    tokens=100,
    email_id="hello@test.com",
    status= True
)
print(res1)

res2 = GeminiResponse(
    output="Hello, how are you",
    tokens="100",
    email_id="hello@test.com",
    status="True"
)
print(res2)