from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

socketio = SocketIO(cors_allowed_origins="*")

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'secret!'
    # CORSを全面許可
    CORS(app, supports_credentials=True)

    from .api import API
    api = API(app)
    from . import ws

    socketio.init_app(app)
    return app