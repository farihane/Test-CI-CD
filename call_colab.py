import requests

# URL publique de ton serveur Colab
GENAI_URL = "https://e9d60ad9df77.ngrok-free.app/hello"

# Option 1 : GET (récupérer un message simple)
response = requests.get(GENAI_URL)
print("Message from Colab (GET):", response.json())

# Option 2 : POST (envoyer un message)
data = {"message": "Hello from Jenkins!"}
response_post = requests.post(GENAI_URL, json=data)
print("Message from Colab (POST):", response_post.json())
