import smtplib, ssl


gmail_user = 'oiunachukwu@gmail.com'
gmail_password = 'your_password'

sent_from = 'Innocent'
to = ['greenboxafrica@gmail.com']
subject = 'Python test mail'
body = 'The mail is sent to you.'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)