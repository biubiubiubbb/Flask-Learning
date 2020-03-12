from flask import Flask, render_template, request, url_for, jsonify, make_response, redirect
from werkzeug.utils import secure_filename
import os
import sys
from flask_api import FlaskAPI

app = FlaskAPI(__name__)
BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))  # 调用该模块的py文件的根目录
app.config.from_pyfile(BASEDIR + '/config.py')


# 检测登陆是否正确
def check_login(username, password):
    print(f'check username:{username} password:{password}')
    if username == 'jake' and password == '123456':
        return True
    else:
        return False


# 主页面index
@app.route('/')
def index():
    return render_template('index.html')


# url参数
@app.route('/show_user/<username>/<password>')
def show_user(username, password):
    print(f'username:{username}, password:{password}')
    return f'username:{username}, password:{password}'


# test
@app.route('/project/')
def project():
    return 'project'


# test
@app.route('/about')
def about():
    return 'about'


# 登陆处理
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print(f'request.cookies:{request.cookies}')
        print('请求登陆页面')
        return render_template('login.html')
    else:
        print('登陆中...')
        print(f'request.cookies:{request.cookies}')
        req_data = request.json
        username = req_data['username']
        password = req_data['password']
        if check_login(username, password):
            print('登陆成功')
            return jsonify({'result': 0})
        else:
            print('登陆失败')
            return jsonify({'result': 1})


# 获取cookie
@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username')
    return username


# 设置cookie
@app.route('/cookie')
def cookie():
    print('cookie')
    resp = make_response(render_template('login.html'))
    resp.set_cookie('username', 'the username')
    return resp


# 上传文件
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('upload.html 没有属性name为file')
            return redirect(request.url)
        file = request.files[
            'file']  # file 在<input type=file name=file>中的name定义
        if file.filename == '':
            print('没有要选择的文件')
            return redirect(request.url)
        file_type = file.filename.split('.')[1].lower()
        if file_type in app.config['ALLOW_EXTENTIONS']:
            filename = secure_filename(file.filename)  # 会去掉中文
            file.save(app.config['UPLOAD_FOLDER'] + filename)
            return jsonify({'result': 0})
        else:
            print('上传的文件名扩展不在列表中')
            return jsonify({'result': 1, 'info': '不允许上传此类文件'})

    else:
        print('请求上传页面')
        return render_template('upload.html')


# 定制404界面
@app.errorhandler(404)
def show_error_page(error):
    return render_template('error_404.html'), 404


@app.route('/<module>/<funcode>')
def test(module, funcode):
    return str(module) + str(funcode)


if __name__ == '__main__':
    # app.run(host=app.config['HOST'], port=app.config['PORT'], debug=True)
    for k, v in app.config.items():
        print(k, v)
