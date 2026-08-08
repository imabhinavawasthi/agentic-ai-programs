import json


def make_gemini_call(config):
    print(config["endpoint"])
    print(config["token"])
    return {
        "status": "success",
        "data": {
            "user_id": config["user_id"],
            "message": "API call successful"
        }
    }

api_config = ""
with open("gemini-api-config.json", "r") as file:
    api_config = json.loads(file.read()) # json string to dict

response = make_gemini_call(api_config)

print(response)

with open("gemini-api-response.json", "w") as file:
    file.write(json.dumps(response)) # dict to json string