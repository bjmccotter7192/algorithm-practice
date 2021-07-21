import smtplib
from email.mime.text import MIMEText

s = smtplib.SMTP('smtp.veteransunited.com')
s.set_debuglevel(1)
msg = MIMEText("""WHAHWEHDSOIFJSDLKFJIO)SDJFKSDJFLKSD""")
sender = 'me@example.com'
recipients = ['bj.mccotter@veteransunited.com', 'allyn.bottorff@veteransunited.com']
msg['Subject'] = "subject line"
msg['From'] = sender
msg['To'] = ", ".join(recipients)
s.sendmail(sender, recipients, msg.as_string())