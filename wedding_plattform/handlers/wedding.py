# coding: utf-8
from tornado.web import RequestHandler


class WeddingHandler(RequestHandler):

    def get(self):
        self.render("wedding.html")
