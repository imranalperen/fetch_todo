import hashlib


def get_access_token(mail):
    pass


def hash_password(string, salt):#string-psw salt-email
    text = string + salt
    hashed_text = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return hashed_text