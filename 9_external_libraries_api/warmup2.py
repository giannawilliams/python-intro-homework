import requests
response = requests.get(
    "https://api.agify.io/?name=michael")

data = response.json()

print(f"Name: {data.get('name')}")
print(f"Age: {data.get('age')}")
print(f"Birthday: {data.get('birthday')}", "No birthday available")