import requests

GENAI_URL = "https://e9d60ad9df77.ngrok-free.app/hello"

response = requests.get(GENAI_URL)
print("Message from Colab:", response.json())
