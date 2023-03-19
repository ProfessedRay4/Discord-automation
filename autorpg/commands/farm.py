import time
import pyautogui
from colorama import Fore

def farm():
    time.sleep(10)
    print(Fore.GREEN + "farming")
    pyautogui.getWindowsWithTitle("Discord")[0].maximize()
    pyautogui.moveTo(765, 993, 2)
    pyautogui.click()
    pyautogui.write('RPG farm')
    time.sleep(.5)
    pyautogui.keyDown('enter')
    print(Fore.GREEN + 'Succesfully did rpg-farm sleeping for 290 seconds')
    time.sleep(294)
    
while True:
    farm()