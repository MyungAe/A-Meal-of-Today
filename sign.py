from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.g8d0ssb.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


# ID, PW, NICK -> DB users에 자징

# 메인 페이지
@app.route('/')
def home():
    return render_template('signin/index.html')

# 회원가입 페이지
@app.route('/makeId')
def singup():
    return render_template('signup/index.html')

# 회원가입 정보 DB 저장
@app.route('/makeNew', methods=["POST"])
def makeNew():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    name_receive = request.form['name_give']

    doc = {
        'id': id_receive,
        'password': pw_receive,
        'nickname': name_receive
    }

    db.users.insert_one(doc)
    return jsonify({'msg': '회원가입 완료!'})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)




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