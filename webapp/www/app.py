import logging
from flask import Flask, request, g
from flask import render_template
import sqlite3

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


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == '123456':
            return render_template('user/user.html', username=username)
    return render_template('user/form.html', error=error, username=username)


if __name__ == '__main__':
    app.run(debug=True)

DATABASE = '/path/to/database.db'


def connect_db():
    return sqlite3.connect(DATABASE)


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request():
    if hasattr(g, 'db'):
        g.db.close()
