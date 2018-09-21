from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) #__name__ это имя теукщего файла app.py (необходимо указывать это отталкивающая точка)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
