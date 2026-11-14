def call_agent_ai_api(
        provider,
        prompt,
        api_key,
        max_tokens,
        **params
):
    print(provider, prompt, api_key, max_tokens)
    if provider=="gemini":
        print(params["gemini_model"])
        print(params["gemini_user_id"])
    elif provider=="openai":
        print(params["openai_email"])
    else:
        print(prompt)



call_agent_ai_api(
    provider="gemini", 
    prompt="What is Python",
    api_key="21343546",
    max_tokens=100, 
    gemini_model="flask-3.5",
    gemini_user_id="3456",
    gemini_password="345364ytegrsfdas"
)

call_agent_ai_api(
    provider="openai", 
    prompt="What is Python",
    api_key="21343546",
    max_tokens=100, 
    openai_email="hello@gmail.com"
)

call_agent_ai_api(
    provider="claude", 
    prompt="What is Python",
    api_key="21343546",
    max_tokens=100, 
    claude_userid = "teytrhfdgd",
    claude_subsib = "qwkafhs"
)