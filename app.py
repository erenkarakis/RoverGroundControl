from flask import Flask
from controllers import MySessionInterface
from views import home, cam_ops, data_ops, user_ops

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    #app.session_interface = MySessionInterface()

    app.register_blueprint(home.bp)
    app.register_blueprint(cam_ops.bp)
    app.register_blueprint(data_ops.bp)
    app.register_blueprint(user_ops.bp)

    return app

