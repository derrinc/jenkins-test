from flask import Flask
from markupsafe import Markup, escape
app = Flask(__name__)

@app.route("/")
def index():
    return("Index!\n")

@app.route("/hello")
def hello():
    return("Hello world!\n")

@app.route("/members")
def members():
    return("Members, hello!\n")

@app.route("/members/<memberName>")
def getMember(memberName):
    return("Hello %s\n" % escape(memberName))

if(__name__ == "__main__"):
    app.run(host="172.31.16.52", port=8080)
