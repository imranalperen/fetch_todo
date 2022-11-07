from backend.db import session
from backend.models import Users
from flask import g
import hashlib
import uuid
import datetime
from datetime import date, timedelta, datetime


def get_access_token(mail):
    access_token = session.query(Users).filter(Users.email==f"{mail}").first()
    return access_token


def db_email_control(form_email):
    return session.query(Users).filter(Users.email == f"{form_email}").first()


def hash_password(string, salt):
    text = string + salt
    hashed_text = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return hashed_text


def db_insert_user(form_email, form_password):
    user = Users(
        email = form_email,
        hashed_password = hash_password(form_password, form_email)
    )
    session.add(user)
    session.commit()