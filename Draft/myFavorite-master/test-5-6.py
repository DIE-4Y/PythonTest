import pymysql
from flask import Flask, request, jsonify
from flask_cors import CORS

# database connect
db = pymysql.connect("127.0.0.1", "root", "myFavorite")
cursor = db.cursor()

app = flask.Flask(__name__)
CORS()
@app.route("")
