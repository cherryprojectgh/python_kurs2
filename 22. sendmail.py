import smtplib
import sys

mail_from = 'Your automation system'
mail_to = 'b.wisien.spam@gmail.com'
mail_subject = 'Processing finished secussfully'
mail_body = 'Siema byku. To jest wiadomość testowa'

message = '''From: {}
Subject: {}
{}
'''.format(mail_from, mail_subject, mail_body)

user = 'b.wisien.spam@gmail.com'
password = '1koT2psy'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465) #wskazanie serwera
    server.ehlo() #przytanie z serwerem
    server.login(user, password)
    server.sendmail(user, mail_to, message)
    server.close()
    print('mail sent')
except:
    print('error sending email')