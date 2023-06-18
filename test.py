import requests
import json

url = "http://127.0.0.1:5000/analyze"

payload = {
    "text": "its a good day for me"
    
}

# Send the POST request with JSON payload
response = requests.post(url, json=payload)

# Print the response
print(response.text)