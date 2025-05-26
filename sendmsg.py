import os
from dotenv import load_dotenv

import requests
import json

load_dotenv()

#Get API variables from env
APIKEY = os.getenv("WA_APIKEY")
URL = os.getenv("WA_URL")

myPhoneNum = os.getenv("PHONENUM")


headers = {
    "Authorization": f"Bearer {APIKEY}",
    "Content-Type": "application/json"
}
data = {
    "messaging_product": "whatsapp",
    "to": f"{myPhoneNum}",
    "type": "text",
    "text": {
        "body": "Testing 123"
    }
}

req = requests.post(URL, headers=headers, json=data)
print("Status:", req.status_code)
print("Response:", req.json())

