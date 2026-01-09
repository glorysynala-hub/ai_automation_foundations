import requests

url = "https://api.agify.io/?name=glory"

response = requests.get(url) #api call

if response.status_code == 200:  #success chheck
    data = response.json()        #convert json to dictionary
    print(f"Name: {data['name']}") #access values
    print(f"Predicted Age: {data['age']}")
else:
    print("Failed to fetch data from API")

#simple rest api call to understand request
