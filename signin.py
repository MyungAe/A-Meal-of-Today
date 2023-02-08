from flask import Flask, render_template
import sign_feat

app = Flask(__name__)
app.register_blueprint(sign_feat.signin)


# GET : 홈페이지
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


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
