import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    EXCEL_FILE_PATH = os.path.join(os.path.dirname(__file__),
                                   'data', 'exam_questions.xlsx')
