from flask import Flask
from config import Configuration

from posts.blueprint import posts


app = Flask(__name__) #__name__ это имя теукщего файла app.py (необходимо указывать это отталкивающая точка)
app.config.from_object(Configuration)

app.register_blueprint(posts, url_prefix='/blog') # регистрируем наш blueprint
