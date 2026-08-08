def make_gemini_api_call(
    prompt: str,
    token: str,
    model: str = "gemini-1.5",
    temperature: float = 0.7,
    max_tokens: int = 200,
    **kwargs
): 
    print(f"Routing request to target model: {model}")
    print(f"Applying dynamic configuration parameters: {kwargs}")
    print("Awaiting API response...\n")
    print(f"Prompt: {prompt}")
    print(f"Token: {token}")

make_gemini_api_call(
    prompt="system_prompt",
    token="your_api_token_here",
    model="gemini-1.5",
    temperature=0.5,
    max_tokens=300,
    top_k=40,  # Example of an extra parameter that will be captured by **
    user_id=12345  # Another example of an extra parameter
)

make_gemini_api_call(
    prompt="new_system_prompt",
    token="your_api_token_here",
    model="gemini-1.5",
    temperature=0.5,
    max_tokens=300,
    top_k=40,  # Example of an extra parameter that will be captured by **
    user_id=12345  # Another example of an extra parameter
)