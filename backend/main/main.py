from flask import(
    Blueprint,
    request,
    jsonify,
    g,
)
from backend.main.decorators import login_required
from backend.main.crud.users_crud import UserCore
from backend.main.crud.todos_crud import TodoCore
from backend.main.utils import create_access_token, send_verify_code, create_verify_code


main = Blueprint("mian", __name__, url_prefix="/api")


@main.route("signup", methods=["POST"])
def signup():
    password = request.json.get("password")
    verify_password = request.json.get("verify_password")
    email = request.json.get("email")
    if password == verify_password:
        if UserCore().register(email, password):
            return jsonify({"response": True})
        
    return jsonify({"response": "Error"}), 401


@main.route("login", methods=["POST"])
def login():
    email = request.json.get("email")
    password = request.json.get("password")
    if UserCore().login(email, password):
        access_token = create_access_token()
        UserCore().update_access_token(email, access_token)

        return jsonify({
            "response": True,
            "access_token": access_token
        })
    
    return jsonify({"response": "Error"}), 401


@main.route("forgot_password", methods=["POST"])
def forgot_password():
    email = request.json.get("email")
    user = UserCore().get_user_by_mail(email)
    if not user:
        return jsonify({"response": False})
    
    verify_code = create_verify_code()
    send_verify_code(email, verify_code)
    
    return jsonify({
        "response": True,
        "verify_code": verify_code
    })


@main.route("forgot_password_endpoint", methods=["POST"])
def forgot_password_endpoint():
    email = request.json.get("email")
    new_password = request.json.get("new_password")
    print(email)
    print(new_password)
    UserCore().update_password(email, new_password)
    
    return jsonify({"response": True})



@main.route("index/add_todo", methods=["POST"])
@login_required
def index_add_todo():
    todo_body = request.json.get("todo")
    TodoCore().add_todo(g.user.id, todo_body)

    return jsonify({"response": True})


@main.route("index/list_todo", methods=["POST"])
@login_required
def index_list_todo():
    todos = TodoCore().get_todos_by_user_id(g.user.id)
    if todos:
        return jsonify({"response": True, "todo_list": todos})

    return jsonify({"response": False})


@main.route("index/done_todo", methods=["DELETE"])
@login_required
def done_todo():
    todo_id = request.json.get("todo_id")
    TodoCore().done_user_todo(todo_id)

    return jsonify({"response": True})


@main.route("index/update_todo", methods=["PATCH"])
@login_required
def update_todo():
    update_body = request.json.get("update_body")
    todo_id = request.json.get("todo_id")
    TodoCore().update_user_todo(g.user.id, update_body, todo_id)

    return jsonify({"response": True})