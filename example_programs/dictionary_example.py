agent1 = {
    "name": "Alice",
    "model": "gpt-4",
    "temperature": 0.7,
    "max_retries": 5,
    "is_active": True
}

agent2 = {
    "name": "Bob",
    "temperature": 0.5,
    "is_active": False
}

# specifically mentioning the key to access the value
print(agent1["name"])  # Output: Alice
print(agent2["model"])  # Output: gemini-2

# you can't define defaults in a dictionary like you can in a dataclass, so you have to ensure all keys are present when creating the dictionary

# there is possibility to miss a key or have a typo in the key name, which can lead to KeyError when trying to access it