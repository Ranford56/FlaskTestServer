from flask import Flask, request, jsonify
import werkzeug

app = Flask(__name__)

@app.route('/upload', methods=["POST"])
def upload():
    if request.method == "POST":
        imageFile = request.files['image']
        fileName = werkzeug.utils.secure_filename(imageFile.filename)
        imageFile.save('./images/' + fileName)
        return jsonify({"message": "Yei"})

if __name__ == "__main__":
    app.run(debug=True, port=4000)