# import smtplib
# import sys
# import functools

# def send_info_mail(user, password, mail_from, mail_to, mail_subject, mail_body):

#     message = '''From: {}
# Subject: {}
# {}
# '''.format(mail_from, mail_subject, mail_body)

#     try:
#         server = smtplib.SMTP_SSL('smtp.gmail.com', 465) #wskazanie serwera
#         server.ehlo() #przytanie z serwerem
#         server.login(user, password)
#         server.sendmail(user, mail_to, message)
#         server.close()
#         print('mail sent')
#     except:
#         print('error sending email')
#         return False

# mail_from = 'Your automation system'
# mail_to = 'b.wisien.spam@gmail.com'
# mail_subject = 'Processing finished secussfully'
# mail_body = 'Siema byku. To jest wiadomość testowa'
# user = 'b.wisien.spam@gmail.com'
# password = '1koT2psy'

# send_info_email_from_gmail = functools.partial(send_info_mail, user, password)
# send_info_email_from_gmail(mail_from, mail_to, mail_subject, mail_body)

import requests 
import os
import functools
 
 
def save_url_file(url, dir, file,msg):
       
    print(msg.format(file))
    
    r = requests.get(url, stream = True) 
    file_path = os.path.join(dir, file)
      
    with open(file_path, "wb") as f: 
        f.write(r.content)
 
 
save_url_to_dir = functools.partial(save_url_file, dir='c:/temp/', msg = 'Please wait: {}')                 
 
url = 'http://mobilo24.eu/spis'
file = 'spis.html'
save_url_to_dir(url = url, file = file)
 
url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
dir = 'c:/temp/'
file = 'logo.png'
save_url_to_dir(url = url, file = file)