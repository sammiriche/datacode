from flask import Flask

app = Flask(__name__)

@app.route('/index/<name>') # /表示具体的URL  它与下面的函数自动绑定
# 这里表示网址的根目录
def test(name):
    return  f'{name} 的第一次'
    return 'first flask'

# def test2():
#     return '非修饰器返回'
# app.add_url_rule('/',endpoint='pick',view_func=test2)

if __name__ == "__main__":
    app.run() # 表示在本地开发服务器上运行该程序
    # flask框架帮你建好了一个测试开发服务器。
    # run里面参数可以选择网站和端口信息
    # 默认端口是5000

