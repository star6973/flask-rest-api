from flask import Flask, Blueprint
from rest_client.example import exam_bp

app = Flask(__name__)
app.register_blueprint(exam_bp, url_prfix="/example")

@app.route("/")
def index():
    return "Index"

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5000)