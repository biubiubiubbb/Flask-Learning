from web.server import app

if __name__ == '__main__':
    print(app.config)
    HOST = app.config['HOST']
    PORT = app.config['PORT']
    app.run(HOST, PORT, debug=True)
