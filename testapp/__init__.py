from flask import Flask
from .extensions import socketio
from .routes import bp
from .utils.camera import generate_frames
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='secret'
    )
    app.register_blueprint(bp)
    
    socketio.init_app(app, cors_allowed_origins="*")

    return app

if __name__ == '__main__':
    app = create_app()
    CORS(app)
    socketio.run(app)
