from flask import Flask

# creating flask application instance
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world"


app.run('0.0.0.0')