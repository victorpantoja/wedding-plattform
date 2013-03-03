# coding: utf-8
from tornado.web import URLSpec

from wedding_plattform.handlers.home import HomeHandler

urls = (
    URLSpec(r'/', HomeHandler, name='home'),
)
