# [Flask Basic Blog Tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/)
## Getting Started
* To open shell (from repo root): `. venv/bin/activate`
* To run (from venv repo root):
    ```
    export FLASK_APP=flaskr
    export FLASK_ENV=development
    flask run
    ```
* To close shell (from venv repo root): `deactivate`
## dependencies
* `python-dotenv`: for keeping secrets secret
## Layout
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in