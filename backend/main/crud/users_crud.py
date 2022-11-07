from backend.db import session
from backend.models import Users
from backend.main.utils import hash_password
from sqlalchemy import and_
import uuid
from datetime import date, timedelta

class UserCore:
    def register(self, form_email, form_password):
        user = session.query(Users).filter(Users.email == f"{form_email}").first()
        if not user:
            user = Users(
                email = form_email,
                hashed_password = hash_password(form_password, form_email)
            )
            session.add(user)
            session.commit()
            return True
        return False #user already registered
    

    def login(self, form_email, form_password):
        hash_psw = hash_password(form_password, form_email)
        user = session.query(Users).filter(and_\
                        (Users.email == f"{form_email}",
                        Users.hashed_password == f"{hash_psw}"))\
                            .first()
        if user:
            return True
        return False
    

    def get_access_token(self, form_email):
        user = session.query(Users).filter(Users.email == f"{form_email}").first()
        if user.access_token:
            return True
        return False


    def create_access_token(self):
        token = uuid.uuid4().hex
        create_date = date.today()
        end_date = create_date + timedelta(days=7)
        token_properties = {
            "token": token,
            "create_date": create_date,
            "end_date": end_date
        }
        return token_properties

    
    def update_access_token(self, form_email, token):
        session.query(Users)\
            .filter(Users.email == f"{form_email}")\
                .update({
                    "access_token": token["token"],
                    "access_token_create_date": token["create_date"],
                    "access_token_expire_date": token["end_date"]
                })
        session.commit()
    

    def get_access_token_expire_date(self, form_email):
        expire_date = session.query(Users).filter(Users.email == f"{form_email}").first()
        return expire_date.access_token_expire_date

    
    def select_access_token(self, form_email):
        user = session.query(Users).filter(Users.email == f"{form_email}").first()
        return user.access_token