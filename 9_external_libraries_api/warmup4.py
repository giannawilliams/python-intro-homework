import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.environ.get("RESTCOUNTRIES_API_KEY")

if not API_KEY:
  print("No API key found. Set RESTCOUNTRIES_API_KEY and try again.")
  exit()

headers = {"Authorization": f"Bearer {API_KEY}"}


try:
   response = requests.get(
    "https://faketesturl.gov", headers=headers)

   if response.status_code != 200:
      print(f"Failed with code {response.status_code}")
      exit()

except requests.exceptions.RequestException:
   print("There is a network error.")
   exit()
