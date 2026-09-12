from flask import json

params = """
{
    "model": "3.7-flash",
    "api_token": "4356yrtewq32456yr",
    "tokens": 100
}
"""

dict1 = json.loads(params)
print(dict1)
print(dict1.get("model"))

params = json.dumps(dict1)
print(params)