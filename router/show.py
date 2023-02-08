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

    #(기능 함) =========== list를 가져와서 삭제할 부분 삭제하고 다시 그 list를 원래 자리에 update 하는 방식============
    restaurants = db.users.find_one({'user.nickname': user_receive}, {'_id': False})['user']['restaurants']

    for i in range(len(restaurants)):
        if restaurants[i]['index'] == int(index_receive):
            del restaurants[i]
            break


    db.users.update_one({'user.nickname': user_receive}, {'$set': {'user.restaurants': restaurants}})

    #(기능 안 됨) Mongodb의 $pull 쿼리를 써서 직접적으로 선택하여 업데이트(삭제) 하는 방법.
    # db.users['user'].update_one({'nickname': user_receive}, {'$pull': {"restaurants": {'index': index_receive}}})

    #(둘다 안 됨)

    # db.users.delete_one({'user.restaurants': {'index': index_receive}})
    # db.users['user']['restaurants'].delete_one({'index': index_receive})
    return jsonify({'msg': '테스트'})
