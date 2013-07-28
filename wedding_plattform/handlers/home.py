# coding: utf-8
from tornado.web import RequestHandler
from wedding_plattform.models.message import Message


class HomeHandler(RequestHandler):

    def get(self):
        messages = Message.all()
        self.render("index.html", messages=messages)
