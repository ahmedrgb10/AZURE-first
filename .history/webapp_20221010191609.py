from flask import Flask
import gw



app = Flask(__name__)

@app.route("/")
def index():
    return gw.info

app.run(host="0.0.0.0",port=5000)


