# coding: utf-8
from tornado.web import RequestHandler


class PartyHandler(RequestHandler):

    def get(self):
        self.render("party.html")
