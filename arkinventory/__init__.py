from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = "0rwJ[>!?9fCh<yAexQt%h>7WJqA;16p?Qd08TfqnzhfKuzJ(uHC.Xg?d6czXM0Fh"

@app.route('/')
def home():
    return "God I do not want to implement routing."

