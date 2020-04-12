import smtplib

smtpObj = smtplib.SMTP('smtp.qq.com', 587)
print(smtpObj.ehlo())
print(smtpObj.starttls())

account = input('Enter qq number: ')
# 授权码
authorization_code = 'glruysrasauwbegg'

print(smtpObj.login(account + '@qq.com', authorization_code))

recipient = input('Enter recipient qq number: ')
msg = 'Subject: Hello Tom Smith'
smtpObj.sendmail(account + '@qq.com', recipient + '@qq.com', msg)
print('Everything Done.')
smtpObj.quit()

"""
(250, b'newxmesmtplogicsvrszc5.qq.com\nPIPELINING\nSIZE 73400320\nSTARTTLS\nAUTH LOGIN PLAIN\nAUTH=LOGIN\nMAILCOMPRESS\n8BITMIME')
(220, b'Ready to start TLS from 111.197.60.45 to newxmesmtplogicsvrszc5.qq.com.')
Enter qq number: ********************
(235, b'Authentication successful')
Enter recipient qq number: ********************
Everything Done.
"""
