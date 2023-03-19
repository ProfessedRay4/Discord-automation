import time
import pyautogui
from art import tprint
from colorama import Fore
import os
import progressbar
import commands
import subprocess
import psutil
import keyboard


tprint(' RPG auto farm ', font="nancyj")

print(Fore.GREEN + 'Farm bot has succesfully initialized...')
time.sleep(1)
print(Fore.BLACK + 'Getting discord application...')
time.sleep(2)
pyautogui.getWindowsWithTitle("Discord")[0].maximize()

print(Fore.BLACK + 'Discord open! beginning farm...')


# fail safe
def close_python_processes():
    processes = psutil.process_iter()
    for process in processes:
        if process.name() == "python.exe":
            process.terminate()
    print(Fore.RED + "All Python processes have been closed.")

keyboard.add_hotkey('f4', close_python_processes)
keyboard.wait('esc')