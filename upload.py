from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:<password>@cluster0.g8d0ssb.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta




@app.route("/upload", methods=["POST"])
def upload_restaurant():

    return jsonify({'msg':'저장 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)