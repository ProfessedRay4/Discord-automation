import time
import pyautogui
from art import tprint
from colorama import Fore

def hunts():
    time.sleep(.7)
    print(Fore.GREEN + "hunting together")
    pyautogui.getWindowsWithTitle("Discord")[0].maximize()
    pyautogui.moveTo(765, 993, 2)
    pyautogui.click()
    pyautogui.write('RPG hunt h t')
    time.sleep(.5)
    pyautogui.keyDown('enter')
    print(Fore.GREEN + 'Succesfully did rpg-hunt and heal sleeping for 30 seconds')
    time.sleep(68.3)

while True:
    hunts()