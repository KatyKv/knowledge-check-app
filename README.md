## Структура проекта
```plaintext
knowledge-check-app/        # Корневая папка проекта
│── app/                    # Основное приложение
│   │── database/           # База данных SQLite
│   │   │── database.db     # Файл базы данных
│   │   │── database.py     # Скрипт работы с БД (создание таблиц, запросы)
│   │── static/             # Статические файлы (CSS, изображения)
│   │── templates/          # HTML-шаблоны
│   │   │── index.html      # Страница входа в тестирование
│   │── __init__.py         # Flask + dotenv
│   │── excel_handler.py    # Чтение и обработка Excel-файла
│   │── results.py          # Сохранение результатов в БД
│   │── routes.py           # Пути Flask (обработчики страниц)
│   │── test_logic.py       # Логика тестирования
│── data/                   # Хранилище данных для тестов
│   │── exam_questions.xlsx # Файл с вопросами
├── .env                    # (добавлен в .gitignore)
├── .gitignore              # Файл игнорирования Git
├── config.py               # Конфигурация проекта
├── LICENSE                 # Лицензия проекта
│── main.py                 # Точка входа, запуск Flask
├── README.md               # Описание проекта
│── requirements.txt        # Зависимости проекта
│── run.sh                  # Автоматизированный запуск без терминала
