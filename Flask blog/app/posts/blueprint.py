from flask import Blueprint
from flask import render_template

from models import Post, Tag

""" первый параметр имя,
#второе путь текeotuj файла, по которому flask будет отталкиваться,
#третье папка с шаблонами
"""

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/')
def index():
    posts = Post.query.all() #записал список постов в переменную post
    return render_template('posts/index.html', posts=posts) #передал список постов в index.html

#получаем урл на пост
@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first() #ищем уникальный пост по slug
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags) #передаем post в шаблон post_detail.html


#http://localhost/blog/tag/python
@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)
