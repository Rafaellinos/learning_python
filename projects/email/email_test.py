import smtplib
# smtp = simple mail transfer protocol
from email.message import EmailMessage

from string import Template # uses to substitute the $ in html file
from pathlib import Path # os.path


html = Template(Path('email.html').read_text())
print(html)

with open("mail_inform.txt", "r") as f:
    user = f.readline() # get your email information
    pwd = f.readline()

email  = EmailMessage() # intanciate the email obj
email['from'] = 'LLIÈGE Suporte'
email['to'] = 'rafael.veloso.lino@hotmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute(name='TinTin'), 'html')
"""
html.substitute > get the $name from html and substitute for TinTin
"""

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() # part of the protocol, like handshake
    smtp.starttls() # encryption connection
    smtp.login(user, pwd)
    smtp.send_message(email)
    print("all good")

