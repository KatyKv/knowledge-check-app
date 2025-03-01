## Структура проекта
```plaintext
test_app/                   # Корневая папка проекта
│── app/                    # Основное приложение
│   │── templates/          # HTML-шаблоны
│   │── static/             # Статические файлы 
│   │── routes.py           # Пути Flask
│   │── excel_handler.py    # Чтение и обработка Excel-файла
│   │── test_logic.py       # Логика тестирования
│   │── results.py          # Сохранение результатов
│── data/                   # Хранилище данных для тестов
│   │── exam_questions.xlsx  # Файл с вопросами
├── .gitignore              # Файл игнорирования Git
├── LICENSE                 # Лицензия проекта
│── main.py                 # Точка входа, запуск Flask
├── README.md               # Описание проекта
│── requirements.txt        # Зависимости проекта
│── run.sh                  # Автоматизированный запуск без терминала
```