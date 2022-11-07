from flask import Flask
from flask_cors import CORS
from backend.main.main import main

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Boşuna_Sayma_Yirmi_Altı_Harfli"
    CORS(app)

    app.register_blueprint(main)

    return app