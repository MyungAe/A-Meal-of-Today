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
    return render_template('signin/index.html')


# POST : 회원가입 정보 전달
@signin.route('/', methods=["POST"])
def save_userdata():
    name_receive = request.form['name_give']
    # print(name_receive)
    users = list(db.users.find({}, {"_id": False, "user.nickname": True}))
    nicknames = []

    for i in range(len(users)):
        nickname = users[i]['user']['nickname']
        nicknames.append(nickname)
    if name_receive in nicknames:
        msg = name_receive + '님, 환영합니다!'
    else:
        doc = {
            'user': {
                'nickname': name_receive,
                'restaurants': []
            }
        }
        db.users.insert_one(doc)
        msg = '가입완료!'
    return jsonify({'nickname': name_receive, 'msg': msg})

