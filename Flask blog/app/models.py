from app import db
from datetime import datetime
from re


def slugify(str):  #pythex.org проверяем регулярку
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', str)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):   # создаем конструктор
        super(Post, self).__init__(*args, **kwargs) # вызываем предка класса Post т.е Model
        self.slug = generate_slug()

    def generate_slug(self):   #генерация заголовка
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)
