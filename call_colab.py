import requests

GENAI_URL = "https://c55b2ab2da49.ngrok-free.app/hello"

logs_data = {
    "logs": "Exemple de log de build Jenkins..."
}

response = requests.post(GENAI_URL, json=logs_data)
try:
    print("Réponse Colab:", response.json())
except ValueError:
    print("Erreur JSON, réponse brute:", response.text)
