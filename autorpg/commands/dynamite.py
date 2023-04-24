import time
import pyautogui
from art import tprint
from colorama import Fore

def bb():
    time.sleep(6)
    print(Fore.GREEN + "bigboat")
    pyautogui.getWindowsWithTitle("Discord")[0].maximize()
    pyautogui.moveTo(765, 993, 2)
    pyautogui.click()
    pyautogui.write('RPG bigboat')
    time.sleep(.5)
    pyautogui.keyDown('enter')
    print(Fore.GREEN + 'Succesfully did bigboat sleeping for 150 seconds')
    time.sleep(189)

while True:
    bb()
