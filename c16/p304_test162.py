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
