from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId
import os

app = Flask(__name__)

mongo_uri  = os.environ.get("MONGO_URI")
db_name    = os.environ.get("DB_NAME")

client = MongoClient(mongo_uri)
mydb = client[db_name]
routercol = mydb["routers"]

@app.route("/")
def main():
    data = routercol.find()
    return render_template("index.html", data=data)

@app.route("/add", methods=["POST"])
def add_comment():
    ip = request.form.get("ip")
    username = request.form.get("username")
    password = request.form.get("password")

    if ip and username and password:
        routercol.insert_one({
            "ip": ip,
            "username": username,
            "password": password
        })
    return redirect(url_for("main"))

@app.route("/delete", methods=["POST"])
def delete_comment():
    try:
        idx = request.form.get("idx")
        routercol.delete_one({'_id': ObjectId(idx)})
    except Exception as e:
        print("Error:", e)
    return redirect(url_for("main"))
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
