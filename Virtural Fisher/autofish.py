import time
import pyautogui
from art import tprint
from colorama import Fore
from random import randint
from pynput.keyboard import Listener
import fade

keyboard_quit = False

def keyboard_handler(key):
    global keyboard_quit
    if hasattr(key, 'char') and key.char == 'q':
        pyautogui.press("backspace")
        print(Fore.RED + "Program closing, please wait")
        keyboard_quit = True

keyboard_listener = Listener(on_press=keyboard_handler)
keyboard_listener.start()



def start():
    print(fade.purplepink("""
                        
      ██╗███╗   ██╗███████╗
      ██║████╗  ██║██╔════╝
      ██║██╔██╗ ██║█████╗  
      ██║██║╚██╗██║██╔══╝  
      ██║██║ ╚████║██║     
      ╚═╝╚═╝  ╚═══╝╚═╝ 

"""))
    print(Fore.GREEN + 'Farm bot has succesfully Initialized...')
    time.sleep(1)
    pyautogui.getWindowsWithTitle('Discord')[0].maximize()
    print(Fore.GREEN + 'Discord open! beginning farm in 5 seconds...')
    print(fade.purpleblue("Press 'q' to close the script"))
    time.sleep(5)

start()
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


while not keyboard_quit:
    fish()





