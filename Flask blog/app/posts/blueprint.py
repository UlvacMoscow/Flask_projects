from flask import Blueprint
from flask import render_template


""" первый параметр имя,
#второе путь текeotuj файла, по которому flask будет отталкиваться,
#третье папка с шаблонами
"""

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/')
def index():
    return render_template('posts/index.html')
