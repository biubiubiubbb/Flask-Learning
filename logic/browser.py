from web.app import router
from web.app import *

@router.route('browser', 'index', 'GET')
def index():
    return render_template(r"C:\Users\SZ02665\Desktop\TEST\VSCode\Python\Flask\web\templates\index.html")

@router.route('browser', 'login', 'GET')
def login_g():
    pass

@router.route('browser', 'login', 'POST')
def login_p():
    pass