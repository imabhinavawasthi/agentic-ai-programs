import json

with open("config.json", "r") as file:
    config_data = file.read()
    config_data = json.loads(config_data)

print(config_data, type(config_data))
print(config_data["model"])


response = {
    "output": "hello, how are you?",
    "tokens_used": 2134,
    "status": "success"
}

with open("output.json", "w") as file:
    file.write(json.dumps(response, indent=4))