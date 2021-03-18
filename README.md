# [Flask Basic Blog Tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/)
## Getting Started
### To activate virtual environment (from repo root): `. venv/bin/activate`
### To run flask app (from venv repo root):
    ```
    export FLASK_APP=flaskr
    export FLASK_ENV=development
    flask run
    ```
### To initialize DB:
  * Open new terminal window
    ```
    (. venv/bin/activate) -- if not in venv already
    export FLASK_APP=flaskr
    export FLASK_ENV=development
    flask init-db
    ```
### To view sqlite data (inside virtual environment):
```
sqlite3
.help -- lists commands (e.g. .database, .tables, .exit etc.)
```
### To close shell (from venv repo root): 
```
deactivate
```
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