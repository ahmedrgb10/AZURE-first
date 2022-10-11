from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "This is my landing page"

app.run(host="0.0.0.0",port=5000)