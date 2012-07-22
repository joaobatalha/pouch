from pouch import app
app.debug = True
if __name__ == '__main__':
               app.run(debug=True, host='0.0.0.0')


# from tornado.wsgi import WSGIContainer
# from tornado.httpserver import HTTPServer
# from tornado.ioloop import IOLoop
# from pouch import app
# app.debug = True
#
# http_server = HTTPServer(WSGIContainer(app))
# http_server.listen(5000)
# IOLoop.instance().start()
