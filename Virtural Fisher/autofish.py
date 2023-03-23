import time
import pyautogui
from art import tprint
from colorama import Fore


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
    print(Fore.GREEN + "fishing...")
    pyautogui.getWindowsWithTitle("Discord")[0].maximize()
    pyautogui.moveTo(460, 985, 2)
    pyautogui.click(x=460, y=985)
    time.sleep(1)
    pyautogui.typewrite('/fish')
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press('enter')
    print(Fore.GREEN + 'Succesfully did /fish sleeping for 4 seconds')
    time.sleep(4)

while True:
    fish()


