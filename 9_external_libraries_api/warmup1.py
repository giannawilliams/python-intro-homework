import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.environ.get("RESTCOUNTRIES_API_KEY")

if not API_KEY:
  print("No API key found. Set RESTCOUNTRIES_API_KEY and try again.")
  exit()

headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.get(
    "https://api.agify.io/?name=michael", headers=headers
)

print(f"Status code: {response.status_code}")
print(f"Response: {response.json()}")