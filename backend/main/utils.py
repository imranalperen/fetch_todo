import hashlib
import uuid
from datetime import timedelta, date
import requests
from backend.localsettings import MAILGUN_API_KEY, MAILGIN_DOMAIN, MAILGIN_TEST_MAIL
import random


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
	return requests.post(
		f"https://api.mailgun.net/v3/{MAILGIN_DOMAIN}/messages",
		auth=("api", f"{MAILGUN_API_KEY}"),
		data={"from": f"{MAILGIN_TEST_MAIL}",
			"to": [f"{user_email}"],
			"subject": "Toddo Reset Password",
			"text": f"{verify_code}"})