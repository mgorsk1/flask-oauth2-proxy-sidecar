from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    email = request.headers.get('X_FORWARDED_EMAIL')
    username = request.headers.get('X_FORWARDED_PREFERRED_USERNAME')

    return f'Hello World {username} {email}!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
