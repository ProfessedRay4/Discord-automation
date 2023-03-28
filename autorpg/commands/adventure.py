import time
import pyautogui
from art import tprint
from colorama import Fore


def adventure():
    time.sleep(18)
    print(Fore.BLUE + "Adventure has started!")
    pyautogui.getWindowsWithTitle("Discord")[0].maximize()
    pyautogui.moveTo(765, 993, 2)
    pyautogui.click()
    pyautogui.write('RPG heal')
    time.sleep(.6)
    pyautogui.keyDown('enter')
    time.sleep(3)
    pyautogui.write('RPG adv h')
    time.sleep(.5)
    pyautogui.keyDown('enter')
    time.sleep(.8)
    pyautogui.write('RPG heal')
    time.sleep(.5)
    pyautogui.keyDown('enter')
    print(Fore.GREEN + 'Succesfully did rpg-adv and rpg-heal sleeping for 1815 seconds')
    time.sleep(2340)
    
while True:
    adventure()