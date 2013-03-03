# coding: utf-8
from tornado.web import RequestHandler


class LinksHandler(RequestHandler):

    def get(self):
        self.render("links.html")
