import requests

url = "https://api.agify.io/?name=glory"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Name: {data['name']}")
    print(f"Predicted Age: {data['age']}")
else:
    print("Failed to fetch data from API")
