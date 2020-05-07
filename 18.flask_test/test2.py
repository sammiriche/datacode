from flask import Flask,redirect,url_for,request

app = Flask(__name__)
@app.route('/success/<name>')
def success(name):
    return f'welcome {name}'

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['kaka'] # kaka相当于变量名
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('kaka')
        return 'nothing'

if __name__ == "__main__":
    app.run('localhost',12306)