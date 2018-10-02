#Model - db часть кода которая отвечает за описание моделей которые хранятся в Database;
#View - отвечает за отображение данных пользователю(то что в Django для этого используют шаблоны );
#Controller - связующие звено: отвечает за запросы от юзера к базе данных, после обработки запросов формируется view >>
#>>(В Django за это отвечает View = Controller);
# За отображение в Django отвечают шаблоны (Templates)


from app import app
from flask import render_template


@app.route('/') # '/' это ключ по которому ищется путь http://127.0.0.1:5000/
#@app.route('/blog') # '/blog' это ключ по которому ищется путь http://127.0.0.1:5000/blog
#{'/' : 'index',
#'/blog' : 'index'}

def index():
    name = 'Ivan'
    return render_template('index.html', n=name)#'Hello world' # можно <h1>'Hello world'</h1> но так лучше не делать используем шаблоны


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
