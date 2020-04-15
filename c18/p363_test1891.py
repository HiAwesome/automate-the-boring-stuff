import pyautogui

"""
Hello world
XYab
print("hello world")!!!

"""

# 运行时请将 4-7 行删除，以便展示效果
pyautogui.click(558, 153)
pyautogui.typewrite('Hello world')

pyautogui.click(558, 179)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])

pyautogui.click(558, 200)
pyautogui.typewrite('print("hello world")!!!')

