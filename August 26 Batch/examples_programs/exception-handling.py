import json


def make_gemini_call(config):
    print(config["endpoint"])


try:
    api_config = ""
    with open("gemini-api-config.json", "r") as file:
        api_config = json.loads(file.read()) # json string to dict

    make_gemini_call(api_config)
except FileNotFoundError as e:
    print("File not found error:", e)
except json.JSONDecodeError as e:
    print("JSON decode error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)