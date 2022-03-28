from flask import Flask, render_template, request
import os, cgi, json

app = Flask(__name__)

@app.route("/")
def index_2():
    return render_template("index_2.html")

@app.route("/submitted", methods=["GET","POST"])
def submitted():
    if request.method == "POST":
        return request.form["user"]

    if request.method == "GET":
        return render_template("index_2.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))