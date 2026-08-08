from dataclasses import asdict, dataclass

@dataclass
class GeminiApiArgs:
    top_k: int
    user_id: int

@dataclass
class GeminiApiCall:
    prompt: str
    token: str
    model: str
    temperature: float
    max_tokens: int
    args: GeminiApiArgs


gemini_call_1 = GeminiApiCall(
    prompt="system_prompt",
    token="your_api_token_here",
    model="gemini-1.5",
    temperature=0.5,
    max_tokens=300,
    args=GeminiApiArgs(top_k=40, user_id=12345)
)

print(gemini_call_1)
print(asdict(gemini_call_1))

def make_gemini_api_call(
        gemini_call: GeminiApiCall
): 
    print(f"Routing request to target model: {gemini_call.model}")
    print(f"Applying dynamic configuration parameters: {gemini_call.args}")
    print("Awaiting API response...\n")
    print(f"Prompt: {gemini_call.prompt}")
    print(f"Token: {gemini_call.token}")

make_gemini_api_call(gemini_call_1)

gemini_call_1.prompt = "new_system_prompt"
make_gemini_api_call(gemini_call_1)