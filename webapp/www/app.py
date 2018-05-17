import logging
from flask import Flask
from flask import render_template

logging.basicConfig(level=logging.INFO)

# 从零开始 写一个webapp， 暂时先使用flask
# 自己研究文档去了

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/user/<username>')
def user(username=None):
    return render_template('user/user.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)

