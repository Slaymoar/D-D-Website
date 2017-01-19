#!/usr/bin/python
import tornado.ioloop
import tornado.web
import os
import json


class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	self.render("d&dhome.html")
#        self.write("The site has loaded.")
#        self.render("static/html/d&dhome.html")

def make_app():
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static")
    }

    return tornado.web.Application([ 
        (r"/", MainHandler),
    ], autoreload=True,
    **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()

#class MainHandler(tornado.web.RequestHandler):
#    def get(self):
