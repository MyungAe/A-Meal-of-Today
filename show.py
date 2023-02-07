from flask import Flask, render_template, request, jsonify

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.g8d0ssb.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('show-resturants/index.html')


@app.route("/show", methods=["POST"])
def show():
    user_receive = request.form['user_give']
    restaurants = db.users.find_one({'user.nickname': user_receive}, {'_id': False})['user']['restaurants']

    return jsonify({'restaurants': restaurants})


@app.route("/delete", methods=["POST"])
def delete():
    user_receive = request.form['user_give']
    index_receive = request.form['index_give']

    restaurants = db.users.find_one({'user.nickname': user_receive}, {'_id': False})['user']['restaurants']

    for i in range(len(restaurants)):
        if int(restaurants[i]['index']) == int(index_receive):
            del restaurants[i]

    db.users.update_one({'user.nickname': user_receive}, {'$set': {'user.restaurants': restaurants}})

    return jsonify({'msg': '테스트'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)