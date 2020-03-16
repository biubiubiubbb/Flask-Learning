from flask import Flask, render_template, request, url_for, jsonify, make_response, redirect
from werkzeug.utils import secure_filename
from flask_api import FlaskAPI

import os
import sys
import traceback

from apis.router_api import Router

#路由表
router = Router()

app = FlaskAPI(__name__)
BASEDIR = os.path.abspath(os.path.dirname(sys.argv[0]))  # 调用该模块的py文件的根目录
app.config.from_pyfile(BASEDIR + '/config.py')
app.config['BASEDIR'] = BASEDIR


@app.route('/browser/<funname>/', methods=['GET', 'POST'])
def api(funname):
    """
    统一路由入口
    """
    try:
        func = router.call(f'browser/{funname}/{request.method}')
        return func()
    except:
        traceback.print_exc()


# 定制404界面
@app.errorhandler(404)
def show_error_page(error):
    return render_template('error_404.html'), 404


if __name__ == '__main__':
    # app.run(host=app.config['HOST'], port=app.config['PORT'], debug=True)
    for k, v in app.config.items():
        print(k, v)
