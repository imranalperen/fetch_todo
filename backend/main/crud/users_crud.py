from backend.db import session
from backend.models import Users
from backend.main.utils import hash_password

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