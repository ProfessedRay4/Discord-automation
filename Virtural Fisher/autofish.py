import time
import pyautogui
from art import tprint, text2art
from colorama import Fore



tprint(' Vfisher auto farm ', font="nancyj")
print(Fore.GREEN + 'Farm bot has succesfully started...')
time.sleep(1)

pyautogui.getWindowsWithTitle("Discord")[0].maximize()

print(Fore.BLACK + 'Discord open! beginning farm.')

# farming
farm = 0

while farm < 5000:
    pyautogui.moveTo(765, 993)
    pyautogui.click()
    pyautogui.write('/fish')
    time.sleep(.5)
    pyautogui.press('tab')
    pyautogui.keyDown('enter')
    print(Fore.GREEN + 'Succesfully did /fish sleeping for 4 seconds')
    time.sleep(3.5)


    farm = +1
