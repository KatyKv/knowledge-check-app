from flask import Blueprint, render_template

from config import Config  # Импортируем конфигурацию
from app.excel_handler import load_questions_from_excel

EXCEL_FILE_PATH = Config.EXCEL_FILE_PATH

bp = Blueprint("routes", __name__)

@bp.route("/")
def index():
    questions = load_questions_from_excel(EXCEL_FILE_PATH)
    return render_template("index.html", questions=questions)
