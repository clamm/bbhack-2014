
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    # read from ${datastore} and push it out
    f = open("datastore")
    return f.readLines()

if __name__ == "__main__":
    app.run()