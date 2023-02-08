

from flask import Blueprint, request, jsonify, render_template
from pymongo import MongoClient

import certifi
import random

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.g8d0ssb.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

select = Blueprint('random_select', __name__, url_prefix="/select")


@select.route('/', methods=["GET"])
def home():
    return render_template('get-random-resturant/index.html')


@select.route("/random", methods=["GET"])
def random_select():
    user_receive = request.args['user_give']
    restaurants = db.users.find_one({'user.nickname': user_receive}, {'_id': False})['user']['restaurants']
    msg = '이건 어떠세요?'

    if len(restaurants) == 0:
        msg = '먼저 맛집을 등록해주세요!'
        random_num = 0
    else :
        random_num = random.randint(1, len(restaurants))

    return jsonify({'restaurants': restaurants, 'random_num': random_num, 'msg': msg})

