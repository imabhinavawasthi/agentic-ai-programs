def make_ai_call(model, token, prompt, **api_params):
    print(f"Model: {model}")
    print(f"Token: {token}")
    print(f"Prompt: {prompt}")

    if model == "gemini":
        print("Using Gemini model for AI call.")
        print("Gemini Region:" + api_params["gemini_region"])
        print("Gemini API Key:" + api_params["gemini_api_key"])
    elif model == "gpt-4":
        print("Using GPT-4 model for AI call.")
        print("GPT-4 API Key:" + api_params["gpt4_api_secret"])
        print("Chatgpt account id:" + api_params["chatgpt_account_id"])
    elif model=="claude":
        print("Using Claude model for AI call.")
        print("Claude API Key:" + api_params["claude_api_key"])
        print("Claude params:" + api_params["claude_params"])


make_ai_call(model="gemini", token="abc123", prompt="What is the capital of France?", gemini_region="us-central1", gemini_api_key="gemini_key_123")

make_ai_call(model="gpt-4", token="xyz456", prompt="What is the capital of France?", gpt4_api_secret="gpt4_secret_456", chatgpt_account_id="chatgpt_account_789")

make_ai_call(model="claude", token="def789", prompt="What is the capital of France?", claude_api_key="claude_key_789", claude_params="some_params")