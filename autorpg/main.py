import time
import pyautogui
from art import tprint
from colorama import Fore
import progressbar
import psutil
import keyboard


tprint(' RPG auto farm ', font="nancyj")

print(Fore.GREEN + 'Farm bot has succesfully initialized...')
time.sleep(1)
print(Fore.BLACK + 'Getting discord application...')
time.sleep(2)
pyautogui.getWindowsWithTitle("Discord")[0].maximize()

print(Fore.BLACK + 'Discord open! beginning farm...')


