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
