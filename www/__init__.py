from flask import Flask
#from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)

    from .views import main_views, user_modify, user_list, refund
    app.register_blueprint(main_views.bp)
    app.register_blueprint(user_list.bp)
    app.register_blueprint(user_modify.bp)
    app.register_blueprint(refund.bp)

    return app
