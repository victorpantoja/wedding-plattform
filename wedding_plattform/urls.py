# coding: utf-8
from tornado.web import URLSpec

from wedding_plattform.handlers.home import HomeHandler
from wedding_plattform.handlers.wedding import WeddingHandler
from wedding_plattform.handlers.party import PartyHandler
from wedding_plattform.handlers.links import LinksHandler
from wedding_plattform.handlers.contacts import ContactsHandler

urls = (
    URLSpec(r'/', HomeHandler, name='home'),
    URLSpec(r'/igreja.html', WeddingHandler, name='wedding'),
    URLSpec(r'/festa.html', PartyHandler, name='party'),
    URLSpec(r'/links.html', LinksHandler, name='links'),
    URLSpec(r'/contato.html', ContactsHandler, name='contacts'),
)
