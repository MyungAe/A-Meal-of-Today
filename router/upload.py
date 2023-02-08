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
    return render_template('upload-resturant/index.html')


@app.route("/upload", methods=["POST"])
def upload_restaurant():
    user_receive = request.form['user_give']
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    if 'm.place.naver.com' in url_receive:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url_receive, headers=headers)
        soup = BeautifulSoup(data.content, 'html.parser')
        data.encoding = 'utf-8'

        name = soup.find("span", {"class": "Fc1rA"}).text
        star = soup.find("span", {"class": "PXMot LXIwF"})
        if star is None:
            star = 'X'
        else:
            star = star.text[2:]
        num_of_reviews = soup.select_one("span.PXMot > a").text[6:]
        addr = soup.find("span", {"class": "LDgIH"}).text
        msg = '등록 완료!'
    else:
        msg = '옳바른 네이버주소가 아니네요ㅠ'

    user = db.users.find_one({'user.nickname': user_receive}, {'_id': False})
    restaurants_len = len(user['user']['restaurants'])

    restaurant = {
        'index': restaurants_len + 1,
        'link': url_receive,
        'name': name,
        'addr': addr,
        'star': star,
        'num_of_reviews': num_of_reviews,
        'comment': comment_receive,
    }

    db.users.update_one({'user.nickname': user_receive}, {'$addToSet': {'user.restaurants': restaurant}})

    return jsonify({'msg': msg})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)