import time
import pyautogui
from art import tprint
from colorama import Fore

def dynamite():
    time.sleep(6)
    print(Fore.GREEN + "dynamite")
    pyautogui.getWindowsWithTitle("Discord")[0].maximize()
    pyautogui.moveTo(765, 993, 2)
    pyautogui.click()
    pyautogui.write('RPG dynamite')
    time.sleep(.5)
    pyautogui.keyDown('enter')
    print(Fore.GREEN + 'Succesfully did rpg-dynamite sleeping for 150 seconds')
    time.sleep(153)

while True:
    dynamite()