from flask import Blueprint, render_template, request, redirect, url_for, flash
from config import Config
from app.excel_handler import load_questions_from_excel
from app.results import save_user_info


EXCEL_FILE_PATH = Config.EXCEL_FILE_PATH

bp = Blueprint("routes", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/start-test", methods=["GET", "POST"])
def start_test():
    error_message = None
    employee_id = ""
    full_name = ""

    if request.method == 'POST':
        employee_id = request.form.get("employee_id").strip()
        full_name = request.form.get("full_name").strip()

        # Валидация табельного номера (8 цифр)
        if not employee_id.isdigit() or len(employee_id) != 8:
            flash("Табельный номер должен содержать ровно 8 цифр.")
            return redirect(url_for("routes.index"))

        # Валидация ФИО (пока просто проверяем, что не пустое, дальше надо подумать)
        if not full_name:
            flash("Введите ваши ФИО.", "error")
            return redirect(url_for("routes.index"))

        # Сохранение пользователя в базе
        error_message = save_user_info(employee_id, full_name)

        if error_message:
            return render_template("index.html",
                                   error_message=error_message,
                                   employee_id=employee_id,
                                   full_name=full_name)

        # Если всё ок, перенаправление пользователя на страницу с тестом
        return redirect(url_for("routes.test_page"))
    return render_template("index.html")

@bp.route("/test")
def test_page():
    questions = load_questions_from_excel(EXCEL_FILE_PATH)
    return "Тут будет тест!"  # Временная заглушка