import json
import requests

api_endpoint = "https://pokeapi.co/api/v2/pokemon/ditto"
# headers = {
#     'accept': 'application/json, text/plain, */*'
# }

# GET
try:
    response = requests.get(api_endpoint)

    # response.raise_for_status() # not successfull
    data = response.json()

    with open("pokemon.json", "w") as file:
        json.dump(data, file)
except Exception as e:
    print("Error:", e)