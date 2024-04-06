from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("pinged")
    return "A message from CS361"