from app.db import session
from app.models import Users
from app.utils import hash_password
from sqlalchemy import and_
from datetime import datetime

class UserCore:
    def register(self, form_email, form_password):
        user = session.query(Users).filter(Users.email == f"{form_email}").first()
        if user:
            return False

        user = Users(
            email = form_email,
            hashed_password = hash_password(form_password, form_email)
        )
        session.add(user)
        session.commit()
        return True


    def login(self, form_email, form_password):
        hash_psw =  hash_password(form_password, form_email)
        user = (
            session.query(Users)
            .filter(and_(
                Users.email == f"{form_email}",
                Users.hashed_password == f"{hash_psw}"
            ))
            .first()
        )
        return user

    
    def update_access_token(self, form_email, token):
        (
            session.query(Users)
            .filter(Users.email == f"{form_email}")
            .update({
                "access_token": token["token"],
                "access_token_expire_date": token["end_date"]
            })
        )
        session.commit()


    def get_user_by_access_token(self, access_token):
        user = session.query(Users).filter(and_(Users.access_token == f"{access_token}", Users.access_token_expire_date > datetime.now())).first()
        return user
    

    def get_user_by_mail(self, form_email):
        user = session.query(Users).filter(Users.email == f"{form_email}").first()
        return user

    def update_password(self, form_email, new_password):
        new_password = hash_password(new_password, form_email)
        (
            session.query(Users)
            .filter(Users.email == f"{form_email}")
            .update({"hashed_password": new_password})
        )
        session.commit()