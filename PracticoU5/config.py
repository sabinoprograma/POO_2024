from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import create_engine

SECRET_KEY = '\xf29k\xc6\xa3/1r\x0c\x14\x11\xeal6\xe1\xf26\x943\x8a\x99\x9a#f'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:4601799@192.168.1.205:3306/logipack'
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()