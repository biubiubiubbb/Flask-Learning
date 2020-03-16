import logic.browser
from web.app import app

if __name__ == '__main__':
    HOST = app.config['HOST']
    PORT = app.config['PORT']
    app.run(HOST, PORT, debug=True)
