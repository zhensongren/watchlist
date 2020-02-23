from flask import Flask
from flask import escape, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
    

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