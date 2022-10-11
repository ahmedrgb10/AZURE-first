from flask import Flask
from gw import info

print("info : ", info)

app = Flask(__name__)

@app.route("/")
def index():
    return info

app.run(host="0.0.0.0",port=5050)


