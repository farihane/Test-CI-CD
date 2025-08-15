import requests

GENAI_URL = "https://c55b2ab2da49.ngrok-free.app/hello"

message_data = {
    "message": "Build completed successfully ✅"
}

try:
    response = requests.post(GENAI_URL, json=message_data)
    print("Server response:", response.json())
except Exception as e:
    print("Error sending message:", e)
