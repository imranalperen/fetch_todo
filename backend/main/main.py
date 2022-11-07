from flask import(
    Blueprint,
    request,
    jsonify,
    g
)
from backend.main.decorators import login_required
from backend.main.crud.users_crud import UserCore
from backend.main.crud.todos_crud import TodoCore
import datetime

main = Blueprint("mian", __name__, url_prefix="/api")

@main.route("signup", methods=["POST"])
def signup():
    password = request.json.get("password")
    verify_password = request.json.get("verify_password")
    email = request.json.get("email")
    if password == verify_password:
        if UserCore().register(email, password):
            return jsonify({"response": "success"})
        
    return jsonify({"response": "Error"}), 401


@main.route("login", methods=["POST"])
def login():
    email = request.json.get("email")
    password = request.json.get("password")
    if UserCore().login(email, password):
        token_expire_date = UserCore().get_access_token_expire_date(email)
        if not token_expire_date or token_expire_date <= datetime.datetime.now():
            token = UserCore().create_access_token()
            UserCore().update_access_token(email, token)
        access_token = UserCore().select_access_token(email)
        return jsonify({
            "response": "success",
            "access_token": access_token
        })
    
    return jsonify({"response": "fail"}), 401


@main.route("index/add_todo", methods=["POST"])
@login_required
def index_add_todo():
    todo = request.json.get("todo")
    print(todo)
    access_token = request.headers.get("Access-Token")
    TodoCore().add_todo(access_token, todo)
    return jsonify({"response": "success"})


@main.route("index/list_todo", methods=["POST"])
@login_required
def index_list_todo():
    pass