import hashlib
import uuid
from datetime import timedelta, date
from localsettings import MAILJET_API_KEY, MAILJET_SECRET_KEY
import random
from mailjet_rest import Client


def hash_password(string, salt):#string-psw salt-email
    text = string + salt
    hashed_text = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return hashed_text


def create_access_token():
    token = uuid.uuid4().hex
    create_date = date.today()
    end_date = create_date + timedelta(days=7)
    token_properties = {
        "token": token,
        "end_date": end_date
    }
    return token_properties


def create_verify_code():
    return random.randint(1000, 9999)


def send_verify_code(user_email, verify_code):
    api_key = MAILJET_API_KEY
    api_secret = MAILJET_SECRET_KEY
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "toddoregister@protonmail.com",
                    "Name": "toddo registration"
                },
                "To": [
                    {
                        "Email": f"{user_email}"
                    }
                ],
                "Subject": "Reset Password",
                "TextPart": "burasi text part",
                "HTMLPart": f"{verify_code}",
                "CustomId": "AppGettingStartedTest"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())