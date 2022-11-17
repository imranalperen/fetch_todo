## Abaut Project
This is my first REST API project. I used flask for api and vanilla js for frontend. My aim of this project learning and understanding server-client relationship, how to work a real webapp product, learning token based user authentication method and reinforce my ORM, js, python-flask skills.

#
<img src="https://i.ibb.co/WFmvKsZ/asd.jpg" alt="drawing" width="550"/>


## How to Run ?

>Before starting, you need a mailjet accaunt to use forgot password feature.
 0. Clone repo
 1. Create a venv in backend directory
 2. Activate venv and install requeriments
 3. Create a `localsettings.py` file in backend directory and set:
```
postgresql = {"pguser": "####",
			"pgpassword": "###",
			"pghost": "localhost",
			"pgport": 5432",
			"pgdb": "####"}

MAILJET_SECRET_KEY = "################"
MAILJET_API_KEY = "################"
```
4. You can run api (backend) with vscode debug, you need to change `"flask_app": "app.py"` to `backend/run.py`, it will run port 5000 default.
5. You can run any html from frontend with live server. vscode live server extension will run in port 5500 default.


#
