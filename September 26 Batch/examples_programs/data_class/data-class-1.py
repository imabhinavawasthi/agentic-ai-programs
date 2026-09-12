from dataclasses import dataclass, asdict
@dataclass
class GeminiInput:
    model: str
    prompt: str
    tokens: int
    temperature=10.0


def call_gemini(geminiInput: GeminiInput):
    print("Model:", geminiInput.model)
    print("Prompt:", geminiInput.prompt)
    print(geminiInput.tokens, geminiInput.temperature)


input = GeminiInput(
    model="3.7-flash",
    prompt="What is OOPs?",
    tokens=100
)

print(asdict(input))

call_gemini(input)

input.prompt = "What is Python?"

call_gemini(input)