# coding: utf-8
from tornado.web import RequestHandler


class ContactsHandler(RequestHandler):

    def get(self):
        self.render("contacts.html")
