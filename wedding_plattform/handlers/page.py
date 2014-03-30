# coding: utf-8
from tornado.web import RequestHandler
#from smtplib import SMTPException
from wedding_plattform import settings
#from wedding_plattform.models.message import Message
#from wedding_plattform.utils.emailhelper import EmailHelper

#import logging


class PageHandler(RequestHandler):

    def get(self, **kwargs):
        if kwargs.get('context'):
            self.render("%s.html" % kwargs['context'],
                        SERVER_NAME=settings.SERVER_NAME)
        else:
            self.render("index.html", SERVER_NAME=settings.SERVER_NAME, messages=[])
    #
    # def post(self, **kwargs):
    #     email = self.request.arguments['p2'][0]
    #     name = self.request.arguments['p1'][0]
    #     message = self.request.arguments['message'][0]
    #
    #     try:
    #         EmailHelper.validateEmail(email)
    #     except Exception, e:
    #         logging.exception(e);
    #
    #     body = """
    #           Dear: <br />
    #            <br />
    #           You've just received a message from %s <%s><br />
    #           ===================================<br />
    #           %s<br />
    #           ===================================<br />
    #           <br />
    #            <br />
    #           The Wedding Plattform Team.
    #           """ % (name, email, message)
    #
    #     try:
    #         mensagem = EmailHelper.mensagem(destinatario="victor.pantoja@gmail.com", corpo=body,
    #             strFrom='Wedding Plattform <mobile.social.share@gmail.com>',
    #             subject="[Wedding Plattform] You've Just Receveid a New Message!")
    #
    #         EmailHelper.enviar(mensagem=mensagem, destinatario="victor.pantoja@gmail.com")
    #     except SMTPException, e:
    #         logging.exception(str(e))
    #
    #     message = Message(message, name, email)
    #     message.save()
    #
    #     self.render("thanks.html", name=name)
