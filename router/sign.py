from flask import Blueprint, render_template, request, jsonify

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.g8d0ssb.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

signin = Blueprint('sign', __name__, url_prefix='/signin')


# GET : 회원가입
@signin.route('/', methods=['GET'])
def home():
    return render_template('signup/index.html')


# POST : 회원가입 정보 전달
@signin.route('/', methods=["POST"])
def save_userdata():
    name_receive = request.form['name_give']
    # print(name_receive)
    doc = {
        'user': {
            'nickname': name_receive,
            'restaurants': []
        }
    }
    db.users.insert_one(doc)
    return jsonify({'nickname': name_receive})

