from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

socketio = SocketIO(cors_allowed_origins="*")

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'secret!'

    from .api import API
    api = API(app)
    from .soc import soc as soc_blueprint
    app.register_blueprint(soc_blueprint)

    socketio.init_app(app)
    CORS(app)
    return app