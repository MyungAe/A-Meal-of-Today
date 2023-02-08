from flask import Flask, render_template

# router
from router import sign, show

app = Flask(__name__)

# blueprints
app.register_blueprint(sign.signin)
app.register_blueprint(show.restaurant)


# GET: 홈페이지
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
