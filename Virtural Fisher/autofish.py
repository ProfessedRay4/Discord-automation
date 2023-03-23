import time
import pyautogui
from art import tprint
from colorama import Fore
from random import randint

tprint(' Vfisher auto farm ', font="nancyj")
print(Fore.GREEN + 'Farm bot has succesfully Initialized...')
time.sleep(1)

discord_window = pyautogui.getWindowsWithTitle('Discord')[0]
discord_window.maximize()

print(Fore.GREEN + 'Discord open! beginning farm in 5 seconds...')
time.sleep(5)


# fishing
farm = 0

def fish():
    sleepy = randint(4, 8)
    pyautogui.getWindowsWithTitle("Discord")[0].maximize()
    print(Fore.BLUE + "fishing...")
    pyautogui.moveTo(460, 985, 2)
    pyautogui.click()
    time.sleep(.5)
    pyautogui.typewrite('/fish')
    time.sleep(.5)
    pyautogui.press("tab")
    time.sleep(.5)
    pyautogui.press('enter')
    print(Fore.GREEN + 'Succesfully did /fish sleeping for {} seconds'.format(sleepy))
    time.sleep(sleepy)

while True:
    fish()


