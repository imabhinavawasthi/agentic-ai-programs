import json
import requests

api_key="<key>"

base_url = "https://generativelanguage.googleapis.com/v1beta"
model = "gemini-2.5-flash" 

# 2. Dynamically construct the endpoint by adding the model to the path
api_endpoint = f"{base_url}/models/{model}:generateContent"
headers = {
    'accept': 'application/json, text/plain, */*',
    'x-goog-api-key': api_key
}
payload = {
    "contents": [{
        "parts": [{
            "text": "Explain what is OOPs in Python?"
        }]
    }]
}

# GET
try:
    response = requests.post(api_endpoint, headers=headers, json=payload)

    response.raise_for_status() # not successfull
    data = response.json()

    with open("api_response.json", "w") as file:
        json.dump(data, file)
except Exception as e:
    print("Error:", e)