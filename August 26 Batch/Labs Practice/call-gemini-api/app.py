import requests

endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

with open("api_key.txt","r") as file:
    api_key = file.read()

headers = {
    "Content-Type": "application/json",
    "X-goog-api-key": api_key
}

payload = {
    "contents": [
        {
        "parts": [
                {
                "text": "What is agentic AI?"
                }
            ]
        }
    ]
}

try:
    response = requests.post(endpoint, headers=headers, json=payload)

    response.raise_for_status()

    data = response.json()

    print(data["candidates"][0]["content"]["parts"][0]["text"])

except Exception as e:
    print(e)