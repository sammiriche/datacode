# from flask import Flask

# app = Flask(__name__)

# @app.route('/kaka/<name>')
# def show(name):
#     return f'欢迎您：{name}'

# if __name__ == "__main__":
#     app.run('localhost',12306)

# from flask import Flask
# app = Flask(__name__)

# @app.route('/zq/<int:tt>')
# def show(tt):
#     return f'欢迎{tt}'

# if __name__ == "__main__":
#     app.run()

from flask import Flask,redirect,url_for
app = Flask(__name__)
@app.route('/admin')
def show_admin():
    return f'欢迎管理员admin'

@app.route('/guest/<guest>')
def shwo_guest(guest):
    return f'欢迎来宾{guest}'

@app.route(('/user/<name>'))
def show_user(name):

    if name == 'admin':
        # return f'欢迎ceshi'
        return redirect(url_for("show_admin"))
    else:
        return redirect(url_for('show_guest',guest = name))


if __name__ == "__main__":
    app.run()