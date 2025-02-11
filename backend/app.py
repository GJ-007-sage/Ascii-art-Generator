from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
import cv2
import time
import numpy as np
import os
from ascii_converter.converter import image_to_ascii


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
cap = cv2.VideoCapture(0)  # Webcam Capture

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_image():
    """Handle image upload and convert to ASCII"""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    image = cv2.imread(filepath)
    ascii_result = image_to_ascii(image)

    return jsonify({"ascii": ascii_result})

def generate_ascii_frames():
    """Capture webcam frames and convert them to ASCII."""
    while True:
        success, frame = cap.read()
        if not success:
            continue

        ascii_frame = image_to_ascii(frame)
        socketio.emit("ascii_frame", {"ascii": ascii_frame})  # Send to frontend
        time.sleep(0.1)  # Control FPS

@socketio.on("connect")
def on_connect():
    """Start streaming on client connection"""
    socketio.start_background_task(generate_ascii_frames)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
