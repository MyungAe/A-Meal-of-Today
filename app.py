from flask import Flask, render_template

app = Flask(__name__)


# GET: 홈페이지
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)