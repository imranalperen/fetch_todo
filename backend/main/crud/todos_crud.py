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

    
    def get_todos_by_user_id(self, user_id):
        rows = session.query(Todos).filter(Todos.user_id == user_id).order_by(desc(Todos.id)).all()
        user_todos = []
        for row in rows:
            temp = {"id": row.id, "todo_body": row.todo_body, "done": row.done}
            user_todos.append(temp)
        
        return user_todos

    
    def done_user_todo(self, todo_id):
        (
            session.query(Todos)
            .filter(Todos.id == todo_id)
            .update({"done": True})
        )
        session.commit()

    
    def update_user_todo(self, token, update_body, todo_id):
        user = session.query(Users).filter(Users.access_token == f"{token}").first()
        (
            session.query(Todos)
            .filter(and_(
                Todos.user_id == user.id,
                Todos.id == todo_id
            ))
            .update({
                "todo_body": update_body,
                "time_updated": datetime.datetime.now()
            })
        )
        session.commit()