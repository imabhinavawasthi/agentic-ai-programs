import json
import requests

api_endpoint = "https://my.newtonschool.co/api/v1/instructor/course/h/88sqmk67n6nl/overview/"
headers = {
    'accept': 'application/json, text/plain, */*',
    'authorization': 'Bearer <token>'
}

# GET
try:
    response = requests.get(api_endpoint, headers=headers)

    # response.raise_for_status() # not successfull
    data = response.json()

    with open("api_response.json", "w") as file:
        json.dump(data, file)
except Exception as e:
    print("Error:", e)