from app import db
from datetime import datetime
import re
from sqlalchemy.sql.functions import current_time

from flask_security import UserMixin, RoleMixin


def slugify(str):  #pythex.org проверяем регулярку
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', str)

#создали таблицу где свезяна posts и tags
post_tags = db.Table('post_tags',
                    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
    )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=current_time())



    def __init__(self, *args, **kwargs):   # создаем конструктор
        super(Post, self).__init__(*args, **kwargs) # вызываем предка класса Post т.е Model
        self.generate_slug()
    #доп свойство кот. выступает связующим звеном между двумя классами Tag & Post
    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

    def generate_slug(self):   #генерация заголовка
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '{}'.format(self.name)


### Flask security

Roles_users = db.Table('roles_users',
            db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
            db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
            )



class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    emeil = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))
