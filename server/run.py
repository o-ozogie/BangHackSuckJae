from flask import Flask
from flask_jwt_extended import JWTManager
from datetime import timedelta

from server.app.api.signup import signup
from server.app.api.login import login
from server.app.api.post import post
from server.app.api.main import mainpg
from server.app.api.me import me
from server.app.api.refresh import refresh

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'variable'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=14)
JWTManager(app)

app.add_url_rule('/signup', 'signup', signup, methods=['POST'])
app.add_url_rule('/login', 'login', login, methods=['POST'])
app.add_url_rule('/post', 'post', post, methods=['POST'])
app.add_url_rule('/main', 'main', mainpg, methods=['GET'])
app.add_url_rule('/me', 'me', me, methods=['GET'])
app.add_url_rule('/refresh', 'refresh', refresh, methods=['GET'])

if __name__ == '__main__':
    app.run()