import os
import sys

HOST = '127.0.0.1'
PORT = 5050
HTTPS = False

base_dir = os.path.abspath(os.path.dirname(sys.argv[0]))

UPLOAD_FOLDER = base_dir + '\\uploads\\'  #上传文件要存储的目录
ALLOW_EXTENTIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsx'}  # 允许上传的文件的扩展名