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
    pyautogui.moveTo(765, 993)
    pyautogui.click()
    pyautogui.write('/fish')
    time.sleep(.5)
    pyautogui.press('tab')
    pyautogui.press('enter')
    print(Fore.GREEN + 'Succesfully did /fish sleeping for 5 seconds...')
    time.sleep(5)
    
while True:
    fish()


