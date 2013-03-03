# coding: utf-8
from tornado.web import RequestHandler


class ContactsHandler(RequestHandler):

    def get(self):
        self.render("contacts.html")

    def post(self):
        arguments = self.request.arguments

        self.render("thanks.html", name=arguments['p1'][0])