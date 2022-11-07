from backend.db import session
from backend.models import Todos, Users


class TodoCore:
    def add_todo(self, token, todo_body):
        user = session.query(Users).filter(Users.access_token == f"{token}").first()
        todo = Todos(todo_body = todo_body, user_id = user.id)
        session.add(todo)
        session.commit()