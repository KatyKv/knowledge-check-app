import openpyxl


def load_questions_from_excel(file_path):
    """Загружает вопросы из Excel-файла и возвращает список словарей"""
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active  # Берем первый (активный) лист

        data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):  # Пропускаем заголовок
            question_id, question, a, b, c, d, num_correct, correct_answers = row

            # Формируем словарь для вопроса
            question_data = {
                "id": question_id,
                "question": question,
                "answers": {"A": a, "B": b, "C": c, "D": d},
                "correct_answers": correct_answers.split(", ") if isinstance(correct_answers, str) else [
                    correct_answers]
            }
            data.append(question_data)

        workbook.close()
        return data
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None