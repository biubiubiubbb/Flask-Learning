from flask import Flask, render_template, request, url_for, jsonify, make_response

app = Flask(__name__)


def check_login(username, password):
    print(f'check username:{username} password:{password}')
    if username == 'jake' and password == '123456':
        return True
    else:
        return False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show_user/<username>/<password>')
def show_user(username, password):
    print(f'username:{username}, password:{password}')
    return f'username:{username}, password:{password}'


@app.route('/project/')
def project():
    return 'project'


@app.route('/about')
def about():
    return 'about'


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


@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username')
    return username

@app.route('/cookie')
def cookie():
    print('cookie')
    resp = make_response(render_template('login.html'))
    resp.set_cookie('username', 'the username')
    return resp

# 定制404界面
@app.errorhandler(404)
def show_error_page(error):
    return render_template('error_404.html'), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)
