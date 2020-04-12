import json, twilio

dic = json.loads(open('/Users/moqi/Documents/Doc/twilio.json').read())
print(dic)
print(dic['sid'])
print(dic['token'])
