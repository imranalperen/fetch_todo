from backend.db import session
from backend.models import Users
from flask import g
import hashlib
import uuid
import datetime
from datetime import date, timedelta, datetime


def get_access_token(mail):
    pass


def hash_password(string, salt):#string-psw salt-email
    text = string + salt
    hashed_text = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return hashed_text