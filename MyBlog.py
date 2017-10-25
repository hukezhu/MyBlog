# encoding=utf8　

import sys
from flask import Flask , request, make_response ,redirect , abort, render_template
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)

bootstrap = Bootstrap(app)


reload(sys)
sys.setdefaultencoding('utf8')

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    #return '<h1>Hello World!</h1> <h2> 你的浏览器是 %s</h2>' % user_agent , 400
    return render_template('index.html')

@app.route('/res')
def testresponse():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    #return response
    return redirect('https://www.baidu.com')#重定向302


@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name = name)
    if name == '张三':
        return '<h1>Hello , %s !</h1>' % name
    else:
        abort(404)
        return '%s 不存在' % name




@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500





if __name__ == '__main__':
    app.run(debug=True)
