from flask import(
    Blueprint,
    request,
    jsonify
)

main = Blueprint("mian", __name__, url_prefix="/api")

@main.route("/test")
def test():
    return "test"