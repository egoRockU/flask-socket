import cv2
from flask_socketio import send, emit
import base64
import time
from flask import current_app
from ..extensions import socketio


def generate_frames(app):
    print('generate frames')
    with app.app_context():
        camera = cv2.VideoCapture('/dev/video0')

        while True:
            success, frame = camera.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                jpg_as_text = base64.b64encode(buffer).decode('utf-8')
                socketio.emit('live_video', jpg_as_text)
                time.sleep(0.1)

        camera.release()