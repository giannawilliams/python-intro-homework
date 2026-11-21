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
    "https://api.restcountries.com/countries/v5/region/Europe?response_fields=names.common,population", headers=headers
)

country = response.json()
countries = country["data"]["objects"]

for count in range (10):
  print(countries[count]['names']['common'])