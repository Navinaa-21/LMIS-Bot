# test_request.py

import requests

url = "http://127.0.0.1:5000/ask"
question = "What is machine learning?"

response = requests.post(url, json={"question": question})
print(response.json())
