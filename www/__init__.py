from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import main_views, user_modify, refund
    app.register_blueprint(main_views.bp)
    app.register_blueprint(user_modify.bp)
    app.register_blueprint(refund.bp)

    return app
