from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def hello_world():
    res = requests.get('https://dummyjson.com/todos')
    return res.json()


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0")
