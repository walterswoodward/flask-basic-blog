import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    ## __name__: name of current Python module
    ## instance_relative_config=True
    app = Flask(__name__, instance_relative_config=True) # create Flask instance
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    # test_config: a dedicated config for testing
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    ## this is where the SQLite database file will be created
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/hello')
    def hello():
        return "Hello World!"

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    from . import db
    db.init_app(app)

    return app