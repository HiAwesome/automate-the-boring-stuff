#! python3
# Automatically fills in the form.

"""
测试问卷地址 https://wj.qq.com/s2/5876762/a132/
"""

import pyautogui, time

nameField = (619, 775)
genderField = (663, 911)
submitField = (890, 1043)
submitColor = (31, 71, 239)
pyautogui.PAUSE = 0.5

formData = []
for i in range(100):
    formData.append({'name': 'zhangsan' + str(i), 'gender': '男' if i % 2 == 0 else '女'})

for person in formData:
    print('>>> 3 Second pause to let user press ctrl-c <<<')
    time.sleep(3)

    while not pyautogui.pixelMatchesColor(submitColor[0], submitColor[1], submitColor[2]):
        print('Wait until the form page has loaded.')
        time.sleep(0.5)

    print('Entering %s info...' % person['name'])

    pyautogui.click(nameField[0], nameField[1])
    pyautogui.typewrite(person['name'])
    pyautogui.click(genderField[0], genderField[1])
    pyautogui.typewrite(person['gender'])

    print('Click submit.')
    pyautogui.click(submitField[0], submitField[1])

    print('Refresh page')
    time.sleep(3)
    pyautogui.hotkey('command', 'r')
