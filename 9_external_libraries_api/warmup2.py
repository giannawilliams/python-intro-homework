import os
from dotenv import load_dotenv
import requests

headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.get(
    "https://api.agify.io/?name=michael", headers=headers
)

data = response.json()

print(f"Name: {data.get('name')}")
print(f"Age: {data.get('age')}")
print(f"Birthday: {data.get('birthday')}", "No birthday available")