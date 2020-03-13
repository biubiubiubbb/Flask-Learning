from logic.browser import *
from logic.postman import *
from web.app import app

if __name__ == '__main__':
    print(router.fundict)
    print('---------------')
    HOST = app.config['HOST']
    PORT = app.config['PORT']
    app.run(HOST, PORT, debug=False)
