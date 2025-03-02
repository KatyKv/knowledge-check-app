from dotenv import load_dotenv
from flask import Flask

load_dotenv() # Загрузка переменных окружения из .env
app = Flask(__name__)

app.config.from_object('config.Config')

from app.routes import bp
app.register_blueprint(bp)
