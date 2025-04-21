import requests
API_URL = "http://localhost:5000/api/secure-data"
TOKEN = "supersecrettoken123"
headers = {
"Authorization": f"Bearer {TOKEN}"
}
response = requests.get(API_URL, headers=headers)
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Failed:", response.status_code, response.text)


API_URL = "http://34.122.125.174:5000/api/time"
TOKEN = "supersecrettoken123"

capital = input("Enter a capital city: ")

headers = {
"Authorization": f"Bearer {TOKEN}",
'capital': capital
}

response = requests.get(API_URL, params=headers)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print('You are required to have a token')
    print("Failed:", response.status_code, response.text)