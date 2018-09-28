from flask import Blueprint
from flask import render_template

from models import Post, Tag
from flask import request

from .forms import PostForm
from app import db
from flask import redirect, url_for


""" первый параметр имя,
#второе путь текeotuj файла, по которому flask будет отталкиваться,
#третье папка с шаблонами
"""

posts = Blueprint('posts', __name__, template_folder='templates')

#http://localhost/blog/create
@posts.route('/create', methods=['POST', 'GET'])
def create_post():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('Something wrong')

        return redirect( url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/')
def index():

    field_query = request.args.get('field_query')

    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if field_query:
        posts = Post.query.filter(Post.title.contains(field_query) | Post.body.contains(field_query)) #.all()
    else:
        posts = Post.query.order_by(Post.created.desc()) #записал список постов в переменную post

    pages = posts.paginate(page=page, per_page=5)

    return render_template('posts/index.html', posts=posts, pages=pages) #передал список постов в index.html

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
