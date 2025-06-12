from time import sleep
import pyautogui # pip install pyautogui


while 1:
    x, y = pyautogui.position()
    pyautogui.moveTo(x + 1, y + 1, 1)
    pyautogui.click()
    sleep(10)
    x, y = pyautogui.position()
    pyautogui.moveTo(x - 1, y - 1, 1)

    pyautogui.click()
    sleep(10)
