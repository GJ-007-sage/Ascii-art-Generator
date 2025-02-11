from flask import Flask, request, render_template, jsonify
from ascii_converter.converter import image_to_ascii
import os
app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")
@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)
    ascii_art = image_to_ascii(file_path)
    return jsonify({"ascii": ascii_art})
if __name__ == "__main__":
    app.run(debug=True)
