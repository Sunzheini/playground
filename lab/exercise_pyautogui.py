import os
from time import sleep

import pyautogui

# ---------------------------------------------------------------------------
# 1. give an image and move mouse to its center
# image = 'D:\\Study\\Projects\\PycharmProjects\\playground\\staticfiles\\image_for_pyautogui.png'
# result = pyautogui.locateOnScreen(image)
# print(result)                       # Box(left=431, top=75, width=75, height=20) // left is x, top is y
# center_coord = pyautogui.center(result)
# print(center_coord)     # center coordinates Point(x=468, y=85)
# pyautogui.moveTo(center_coord)     # moves mouse

# sleep(2)
#
# # ---------------------------------------------------------------------------
# # 2. search in YouTube
# search_word = pyautogui.prompt(text='', title='Enter search word in youtube')
#
# pyautogui.click()
# sleep(1)
#
# pyautogui.hotkey('ctrl', 't')
# sleep(1)
#
# .write('https://www.youtube.com/')
# pyautogui.hotkey('enter')
# sleep(1)
#
# image2 = 'D:\\Study\\Projects\\PycharmProjects\\playground\\staticfiles\\image_for_pyautogui2.png'
# x, y = pyautogui.locateCenterOnScreen(image2, confidence=0.9)
# pyautogui.moveTo(x, y, 1)
# pyautogui.click()
# sleep(1)
#
# pyautogui.write(search_word)
# pyautogui.hotkey('enter')


while 1:
    sleep(600)
    pyautogui.hotkey('space')
    sleep(600)
    pyautogui.hotkey('space')
