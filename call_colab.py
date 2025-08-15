import requests

GENAI_URL = "https://c55b2ab2da49.ngrok-free.app/hello"

# GET
response = requests.get(GENAI_URL)
try:
    print("Message from Colab (GET):", response.json())
except ValueError:
    print("GET Response is not JSON:", response.text)

# POST
data = {"message": "Hello from Jenkins!"}
response = requests.post(GENAI_URL, json=data)
try:
    print("Message from Jenkins (POST):", response.json())
except ValueError:
    print("POST Response is not JSON:", response.text)
