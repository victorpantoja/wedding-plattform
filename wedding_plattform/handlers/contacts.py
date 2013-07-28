# coding: utf-8
from smtplib import SMTPException
from tornado.web import RequestHandler
from wedding_plattform.utils.emailhelper import EmailHelper
from wedding_plattform.models.message import Message

import logging


class ContactsHandler(RequestHandler):

    def get(self):
        self.render("contacts.html")

    def post(self):
        email = self.request.arguments['p2'][0]
        name = self.request.arguments['p1'][0]
        message = self.request.arguments['message'][0]

        try:
            EmailHelper.validateEmail(email)
        except Exception, e:
            logging.exception(e);

        body = """
              Dear: <br />
               <br />
              You've just received a message from %s <%s><br />
              ===================================<br />
              %s<br />
              ===================================<br />
              <br />
               <br />
              The Wedding Plattform Team.
              """ % (name, email, message)

        try:
            mensagem = EmailHelper.mensagem(destinatario="victor.pantoja@gmail.com", corpo=body,
                strFrom='Wedding Plattform <mobile.social.share@gmail.com>',
                subject="[Wedding Plattform] You've Just Receveid a New Message!")

            #EmailHelper.enviar(mensagem=mensagem, destinatario="victor.pantoja@gmail.com")
        except SMTPException, e:
            logging.exception(str(e))

        message = Message(message, name, email)
        message.save()

        self.render("thanks.html", name=name)
