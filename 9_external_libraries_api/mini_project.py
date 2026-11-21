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
    "https://api.restcountries.com/countries/v5?response_fields=names.common,capitals,region,population",headers=headers)
  
   if response.status_code != 200:
     print(f"Failed with code {response.status_code}")
     exit()

except requests.exceptions.RequestException:
   print("There is a network error.")



country_dict = response.json()
country_info = country_dict["data"]["objects"]

countries = []

for item in country_info:
    capital = item["capitals"][0]["name"] if item.get("capitals") else "N/A"
    country_entry = {
       "name": item['names']['common'],
       "capital": capital,
       "region": item['region'],
       "population": item['population'],
      }

    countries.append(country_entry)

while True:
    print("Loaded countries:", len(countries))
    menu = input("== Country Explorer ==\n 1. Search by name \n 2. Filter by region \n 3. Quit \n Choose an option (1-3):\n")
    
    if menu == "1":
        name_search = input("Enter search term: ").strip()
        print(f"Search: {name_search}\n")

        name_matches = [
           country
           for country in countries
           if name_search.lower() in country["name"].lower()
        ]
   
        if not name_matches:
           print("No matching countries found.") 
        else:
           for country in name_matches:
              print(f"{country['name']} — Capital: {country['capital']} | Region: {country['region']} | Population: {country['population']:,}")

    if menu == "2":
       region_search = input("Enter region to search: ").strip()
       print(f"Search: {region_search}\n")

       sorted_countries = sorted(countries, key=lambda country: country['population'] or 0, reverse=True)

       region_matches = [
          country
          for country in sorted_countries
          if region_search.lower() in (country['region'] or "").lower()
       ]

       if not region_matches:
          print(f"No countries in the region of {region_search} found.")
       else:
          for country in region_matches:
             print(f"{country['name']} — Capital: {country['capital']} | Region: {country['region']} | Population: {country['population']:,}")

    if menu== "3":
       break



       


