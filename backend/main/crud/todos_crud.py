from backend.db import session
from backend.models import Todos, Users
from sqlalchemy import desc, and_
import datetime


class TodoCore:
    def add_todo(self, token, todo_body):
        user = session.query(Users).filter(Users.access_token == f"{token}").first()
        todo = Todos(todo_body = todo_body, user_id = user.id)
        session.add(todo)
        session.commit()

    
    def get_users_todos_by_acctoken(self, token):
        user = session.query(Users).filter(Users.access_token == f"{token}").first()
        rows = session.query(Todos).filter(Todos.user_id == user.id).order_by(desc(Todos.id)).all()
        user_todos = []
        for row in rows:
            user_todos.append(row.todo_body)
        
        return user_todos

    
    def delete_todo_by_token(self, token, body):
        user = session.query(Users).filter(Users.access_token == f"{token}").first()
        todo = session.query(Todos).filter(and_\
            (Users.id == user.id, Todos.todo_body == f"{body}")).first()
        session.delete(todo)

    
    def update_todo(self, token, update_body, old_body):
        user = session.query(Users).filter(Users.access_token == f"{token}").first()
        session.query(Todos).filter(and_\
            (Todos.user_id == user.id, Todos.todo_body == old_body))\
                .update({
                    "todo_body": update_body,
                    "time_updated": datetime.datetime.now()
                })
        session.commit()