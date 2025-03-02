from datetime import datetime
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__),
                       "database", "database.db")

def save_user_info(employee_id, full_name):
    """Сохраняет информацию о пользователе в базе данных перед началом теста."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Проверка, существует ли пользователь с таким employee_id
    cursor.execute("SELECT id, full_name FROM users WHERE employee_id = ?", (employee_id,))
    user = cursor.fetchone()

    if user:
        # Если пользователь найден, проверяем, совпадает ли имя
        if user[1] != full_name:
            conn.close()
            return "Ошибка: табельный номер уже зарегистрирован с другим ФИО!"

        # Если имя совпадает, добавляем новое время входа
        login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO test_results (user_id, date, score, correct_answers) VALUES (?, ?, ?, ?)",
                       (user[0], login_time, 0, ""))  # Пока записываем пустые значения для score и correct_answers
    else:
        # Если пользователь новый, добавляем его в таблицу users
        cursor.execute("INSERT INTO users (employee_id, full_name) VALUES (?, ?)", (employee_id, full_name))
        user_id = cursor.lastrowid  # Получаем ID нового пользователя
        login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO test_results (user_id, date, score, correct_answers) VALUES (?, ?, ?, ?)",
                       (user_id, login_time, 0, ""))  # Записываем первый результат

    conn.commit()
    conn.close()