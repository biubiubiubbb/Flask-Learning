from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, url_for, jsonify, make_response, redirect

from web.app import router, app
from utils.file import CFile


# index.html
@router.route('browser', 'index', 'GET')
def index():
    url = '127.0.0.1:5050/index'
    my_list = [1, 3, 5, 7]
    my_dict = {'username': 'jake', 'age': 18}
    return render_template('index.html',
                           my_list=my_list,
                           my_dict=my_dict,
                           url=url)


# login.html
@router.route('browser', 'login', 'GET')
def login_g():
    return render_template('login.html')


# 登陆请求
@router.route('browser', 'login', 'POST')
def login_p():
    req_data = request.json
    return jsonify({'result': req_data['result']})


# set cookie test
@router.route('browser', 'set_cookie', 'GET')
def set_cookie():
    resp = make_response(render_template('login.html'))
    resp.set_cookie('username', 'qinxi')
    return resp


# get cookie test
@router.route('browser', 'get_cookie', 'GET')
def get_cookie():
    username = request.cookies.get('username')
    return f"get username:{username} from cookie"


# upload.html
@router.route('browser', 'upload', 'GET')
def upload_file_g():
    return render_template('upload.html')


# 上传文件请求
@router.route('browser', 'upload', 'POST')
def upload_file_p():
    if 'file' not in request.files:
        print('upload.html 没有属性name为file')
        return redirect(request.url)
    file = request.files['file']  # file 在<input type=file name=file>中的name定义
    if file.filename == '':
        print('没有要选择的文件')
        return redirect(request.url)
    file_type = CFile.getFileType(file.filename)
    if file_type in app.config['ALLOW_EXTENTIONS']:
        filename = secure_filename(file.filename)  # 会去掉中文
        file_full_path = app.config['UPLOAD_FOLDER'] + filename
        CFile.mkfileIfNotExist(file_full_path)
        file.save(file_full_path)
        return jsonify({'result': 0})
    else:
        print('上传的文件名扩展不在列表中')
        return jsonify({'result': 1, 'info': '不允许上传此类文件'})
