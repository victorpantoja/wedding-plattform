# coding: utf-8
from smtplib import SMTPException
from tornado.web import RequestHandler
from wedding_plattform.utils.emailhelper import EmailHelper

import logging


class ContactsHandler(RequestHandler):

    def get(self):
        self.render("contacts.html")

    def post(self):
        arguments = self.request.arguments
        email = arguments['p2'][0]
        name=arguments['p1'][0]

        try:
            EmailHelper.validateEmail(email)
        except Exception, e:
            logging.exception(e);

        body = """
              Dear: <br />
               <br />
              You've just received a message from %s <%s><br />
              ===================================<br />
              Example<br />
              ===================================<br />
              <br />
               <br />
              The Wedding Plattform Team.
              """ % (name, email)

        try:
            mensagem = EmailHelper.mensagem(destinatario="victor.pantoja@gmail.com", corpo=body,
                strFrom='Wedding Plattform <mobile.social.share@gmail.com>',
                subject="[Wedding Plattform] You've Just Receveid a New Message!")

            EmailHelper.enviar(mensagem=mensagem, destinatario="victor.pantoja@gmail.com")
        except SMTPException, e:
            logging.exception(str(e))

        self.render("thanks.html", name=name)
