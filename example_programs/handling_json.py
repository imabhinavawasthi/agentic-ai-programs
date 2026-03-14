import json

user_data = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "subject": {
        "name": "Mathematics",
        "code": "MATH101"
    },
    "grades": [85, 90, 78]
}

# Convert the Python dictionary to a JSON string
json_string = json.dumps(user_data, indent=4)
print("JSON String:")
print(json_string)

# Convert the JSON string back to a Python dictionary
parsed_data = json.loads(json_string)
print("\nParsed Data:")
print(parsed_data)