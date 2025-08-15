import requests

GENAI_URL = "https://c55b2ab2da49.ngrok-free.app/hello"

response = requests.get(GENAI_URL)
print("Message from Colab:", response.json())
# Envoyer un message simple à Colab (POST)

data = {"message": "Hello from Jenkins!"}
response = requests.post(GENAI_URL, json=data)

print("Message from Jenkins:", response.json())
