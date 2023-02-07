from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi

app = Flask(__name__)
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.g8d0ssb.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


# GET : 홈페이지
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


# GET : 회원가입
@app.route('/signin')
def signin():
    return render_template('signup/index.html')


# POST : 회원가입 정보 전달
@app.route('/signin', methods=["POST"])
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
    return jsonify({'msg': '회원가입 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)

# # 아이디 중복확인 GET
# @app.route('/overlapId', methods=['GET'])
# def overlapId():
#     users_list = list(db.users.find({}, {'_id': False}))
#     return jsonify({'users': users_list})
# # 닉네임 중복확인 GET
# @app.route('/overlapName', methods=['GET'])
# def overlapName():
#     users_list = list(db.users.find({}, {'_id': False}))
#     return jsonify({'users': users_list})

# # 로그인 GET
# @app.route('/signin', methods=["GET"])
# def signin_post():
#     users_list = list(db.users.find({}, {'_id': False}))
#     return jsonify({'users': users_list})
