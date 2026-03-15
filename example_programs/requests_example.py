import json
import requests
from pydantic import BaseModel
from typing import List, Optional

class Lecture(BaseModel):
    hash: str
    title: str
    start_timestamp: int
    rating: float
    attendance: int
    understanding: Optional[float]  # Assuming it can be float or null

class LectureOverviewResponse(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Lecture]

# URL
url = 'https://my.newtonschool.co/api/v1/instructor/course/h/qbtmvm2he927/lecture_overview/'

# Query parameters
params = {
    'limit': 15,
    'offset': 0
}

# Headers including auth
headers = {
    'accept': 'application/json, text/plain, */*',
    'authorization': 'Bearer your_access_token_here',
    'client-id': 'your_client_id_here',
    'client-secret': 'your_client_secret_here',
}

# Make the request
response = requests.get(url, headers=headers, params=params)

# Check if successful
if response.status_code == 200:
    data = response.json()
    # Parse into Pydantic model
    lecture_response = LectureOverviewResponse(**data)
    print("Parsed response:")
    print(lecture_response)
    with open('lecture_overview_response.json', 'w') as f:
        json.dump(data, f, indent=4)
else:
    print(f"Error: {response.status_code}")
    print(response.text)