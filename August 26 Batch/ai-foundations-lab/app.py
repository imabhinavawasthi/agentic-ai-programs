users_database = [
    {"id": 101, "name": "Alice", "role": "admin", "is_active": True},
    {"id": 102, "name": "Bob", "role": "user", "is_active": False},
    {"id": 103, "name": "Charlie", "role": "editor", "is_active": True}
]

active_users = []
context = ""
for i, user in enumerate(users_database):
    if user["is_active"]:
        active_users.append(user["name"])
        context += f"User {i + 1}: {user['name']}\n"

print(context)

system_prompt = f"""
System Instruction: You are a corporate communication assistant.
Task: Write a highly professional welcome message for the following active team members.

Active Members:
{context}
Please keep the tone encouraging and brief.
"""

print(system_prompt)

def execute_mock_llm_call(prompt_text, model_engine="gpt-4", **kwargs):
    print(f"Routing request to target model: {model_engine}")
    
    # Notice how **kwargs automatically bundles extra arguments into a dictionary
    print(f"Applying dynamic configuration parameters: {kwargs}")
    print("Awaiting API response...\n")
    
    return f"Mock API Output: Welcome aboard, {', '.join(active_users)}! Let's get to work."

api_response = execute_mock_llm_call(
        prompt_text=system_prompt,
        model_engine="gpt-4-turbo",
        temperature=0.4,       # OpenAI specific
        max_tokens=250,        # Standard sizing
        top_k=50               # Anthropic specific (caught perfectly by **kwargs)
    )

print(api_response)