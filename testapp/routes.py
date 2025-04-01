from flask import Blueprint, current_app, make_response, jsonify
from .extensions import socketio
from flask_socketio import send, emit
from .utils.camera import generate_frames
from flask_cors import cross_origin

bp = Blueprint('index', __name__)

@bp.route("/")
def index():
    return "Hello Worlds"

@bp.route("/click")
@cross_origin()
def click():
    response = make_response(jsonify({"message":"Clicked!(this message is from server btw)"}))
    print("button has been clicked!")
    return response


@socketio.on('connect')
def handle_connect():
    print('client connected')
    app = current_app._get_current_object()
    socketio.start_background_task(generate_frames, app)

@socketio.on('message')
def handle_message(data):
    emit('receive_message', data, broadcast=True)

@socketio.on('get_video')
def handle_video():
    print('handle_video')
    generate_frames()