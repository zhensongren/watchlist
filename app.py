from flask import Flask, render_template
from flask import escape, url_for

app = Flask(__name__)
name = 'Zhensong Ren'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)
    

@app.route('/user/<name>')
def user_page(name):
    #return 'Hello %s' % escape(name)
    return f'Hello {escape(name)}!'

@app.route('/test')
def test():
    print(url_for('user_page', name='zhensong'))
    print(url_for('hello'))
    print(url_for('test', num=8))
    return 'This is a test page for url_for function'