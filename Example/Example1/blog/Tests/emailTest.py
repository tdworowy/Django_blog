from django.core import mail
from django.conf import settings
import os
from django.core.wsgi import get_wsgi_application
import django

settings.configure()
django.setup()
#

from django.test import TestCase


class EmailTest(TestCase):

    def test_send_email(self):
        print("Test")
        connection = mail.get_connection()
        connection.open()
        email = mail.EmailMessage('Django mailTEST', 'email from django', 'testaccouny123321@gmail.com',
                                  ['testaccouny123321@gmail.com'], connection=connection)

        email.send()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Django mail')
        connection.close()
        # Don't work
