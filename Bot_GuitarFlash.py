import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1333,880,(0,152,0)):
        pyautogui.press('a')
        sleep(0.01)
    if pyautogui.pixelMatchesColor(1445,876,(255,0,0)):
        pyautogui.press('s')
        sleep(0.01)
    if pyautogui.pixelMatchesColor(1662,874,(0,141,236)):
        pyautogui.press('k')
        sleep(0.01)
    if pyautogui.pixelMatchesColor(1551,877,(244,244,2)):
        pyautogui.press('j')
        sleep(0.01)