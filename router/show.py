from flask import Blueprint, request, jsonify, render_template
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.g8d0ssb.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

restaurant = Blueprint('show', __name__, url_prefix="/restaurant")


@restaurant.route('/', methods=["GET"])
def home():
    return render_template('show-resturants/index.html')


@restaurant.route("/show", methods=["GET"])
def show():
    user_receive = request.args['user_give']
    restaurants = db.users.find_one({'user.nickname': user_receive}, {'_id': False})['user']['restaurants']
    return jsonify({'restaurants': restaurants})


@restaurant.route("/delete", methods=["DELETE"])
def delete():
    user_receive = request.form['user_give']
    index_receive = request.form['index_give']

    print(user_receive, index_receive)

    restaurants = db.users.find_one({'user.nickname': user_receive}, {'_id': False})['user']['restaurants']

    for i in range(len(restaurants)):
        # print(restaurants[i]['index'], index_receive)
        if restaurants[i]['index'] == int(index_receive):
            # print(i, restaurants[i])
            del restaurants[i]
            break
    # print(restaurants)

    #데이터 삭제 후 바로 index 조정

    for i in range(len(restaurants)):
        new_index = i + 1
        restaurants[i]['index'] = new_index

    db.users.update_one({'user.nickname': user_receive}, {'$set': {'user.restaurants': restaurants}})

    return jsonify({'msg': '테스트'})
