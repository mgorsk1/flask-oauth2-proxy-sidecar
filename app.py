import jwt
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    _token = request.headers.get('X_FORWARDED_ACCESS_TOKEN')

    data = jwt.decode(_token, algorithms=['RS256'], options={"verify_signature": False})

    email = data.get('email')
    username = data.get('name')

    return f'Hello {username} ({email})!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
