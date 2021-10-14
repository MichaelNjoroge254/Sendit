from os import environ
from django.core.mail import EmailMessage





class Util:
    @staticmethod
    def send_email(data):
        email=EmailMessage(from_email=environ.get('EMAIL_HOST_USER'),subject=data['email_subject'],body=data['email_body'],to=[data['to_email']])
        email.send()