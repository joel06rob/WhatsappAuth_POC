import os
from dotenv import load_dotenv
from twilio.rest import Client

import requests
import json
import secrets
import time
import re

load_dotenv()

#Get API variables from env
APIKEY = os.getenv("AUTH_TOKEN")
SID = os.getenv("ACC_SID")
fromNum = os.getenv("TWILIO_PHONE")

#Query User's Phone Number

print("Hello, to recieve your 6 digit authentication code. Enter a UK phone number below:")

while True:
    enteredNum = input("(+44): ").strip().replace(" ", "")

    #Validation
    if re.match(r'^(0?7\d{9})$', enteredNum):
        if enteredNum.startswith("0"):
            enteredNum = enteredNum[1:]
    
        phoneNum = "44" + enteredNum
        break
    else:
        print("Incorrect UK phone number format, try again:")



#Get a 6 digit auth code and start Auth timer.
generated_AuthToken = secrets.randbelow(900000) + 100000
timer_AuthStart = time.time()

#Message Request - Twilio
client = Client(SID, APIKEY)

message = client.messages.create(
    from_=f"{fromNum}",
    to=f"whatsapp:+{phoneNum}",
    body=f"Your Authentication Code is {generated_AuthToken}"
)

print("Auth Token Sent!")

try:
    #Enter Auth Token to confirm.
    user_AuthToken = int(input("Please Enter 6 Digit Code Sent: "))
    timer_AuthEnd = time.time() - timer_AuthStart

    if not user_AuthToken == generated_AuthToken or timer_AuthEnd > 120:
        print("Incorrect Code - You are not authorized!")
    else:
        print("Correct - Welcome!")
except ValueError:
    print("Incorrect Code - You did not enter a 6 digit code!")