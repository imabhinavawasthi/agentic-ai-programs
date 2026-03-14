def call_ai_agent(agent_name, token, **kwargs):
    print(f"Calling AI agent: {agent_name}")
    print(f"Token: {token}")
    print(f"Additional arguments: {kwargs}")
    if agent_name == "gemini":
        print("text",kwargs.get("text"))
        print("image",kwargs.get("image"))
    elif agent_name == "gpt-4":
        print("text",kwargs.get("text"))
        print("code",kwargs.get("code"))
    elif agent_name == "claude":
        print("code",kwargs.get("code"))

call_ai_agent("gemini","keuhfikhewcdosiljfewoicdsl", text="Hello, how are you?", image="image_data", name="abhinav")
call_ai_agent("gpt-4","keuhfikhewcdosiljfewoicdsl", text="Hello, how are you?", code="print('Hello, World!')", name="abhinav")
call_ai_agent("claude","keuhfikhewcdosiljfewoicdsl", code="print('Hello, World!')", name="abhinav")

################################

def call_gemini_agent(token, text, code):
    print(f"Calling Gemini agent with token: {token}")
    print(f"Text: {text}")
    print(f"Code: {code}")

def call_gpt4_agent(token, text, image):
    print(f"Calling GPT-4 agent with token: {token}")
    print(f"Text: {text}")
    print(f"Image: {image}")

def call_claude_agent(token, code):
    print(f"Calling Claude agent with token: {token}")
    print(f"Code: {code}")

call_gemini_agent("keuhfikhewcdosiljfewoicdsl", "Hello, how are you?", "print('Hello, World!')")
call_gpt4_agent("keuhfikhewcdosiljfewoicdsl", "Hello, how are you?", "image_data")
call_claude_agent("keuhfikhewcdosiljfewoicdsl", "print('Hello, World!')")