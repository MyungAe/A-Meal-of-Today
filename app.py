from flask import Flask, render_template

# router
from router import sign, show, upload, random_select

app = Flask(__name__)

# blueprints
app.register_blueprint(sign.signin)
app.register_blueprint(show.restaurant)
app.register_blueprint(upload.register)
app.register_blueprint(random_select.select)


# GET: 홈페이지
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
