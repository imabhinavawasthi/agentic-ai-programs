from pydantic import BaseModel, EmailStr, PositiveInt, ValidationError

class LLMResponse(BaseModel):
    answers: str
    lines: PositiveInt
    code: str
    email: EmailStr


def call_llm(prompt):
    print("Prompt:", prompt)

    # gemini api is called

    return {
        "answers": "delhi",
        "lines": "-12",
        "code": "def ......",
        "email": "hello@google.com"
    }

def validate_parse_response():
    try:
        response = call_llm("Captial of India")
        validated_response = LLMResponse(**response)
        print(validated_response)
    except ValidationError as e:
        print("Validation Error:", e)


validate_parse_response()