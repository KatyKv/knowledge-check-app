## Структура проекта
```plaintext
knowledge-check-app/        # Корневая папка проекта
│── app/                    # Основное приложение
│   │── static/             # Статические файлы
│   │── templates/          # HTML-шаблоны
│   │── __init__.py         # Flask + dotenv
│   │── excel_handler.py    # Чтение и обработка Excel-файла
│   │── results.py          # Сохранение результатов
│   │── routes.py           # Пути Flask
│   │── test_logic.py       # Логика тестирования
│── data/                   # Хранилище данных для тестов
│   │── exam_questions.xlsx  # Файл с вопросами
├── .env                    # (добавлен в .gitignore)
├── .gitignore              # Файл игнорирования Git
├── config.py               # Лицензия проекта
├── LICENSE                 # Лицензия проекта
│── main.py                 # Точка входа, запуск Flask
├── README.md               # Описание проекта
│── requirements.txt        # Зависимости проекта
│── run.sh                  # Автоматизированный запуск без терминала
```