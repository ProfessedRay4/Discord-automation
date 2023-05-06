import time
import threading
import time
import pyautogui
from art import tprint
from colorama import Fore
import fade
import os

def start():
    print(fade.purplepink("""
 █████  ██    ██ ████████  ██████      ██████  ██████   ██████  
██   ██ ██    ██    ██    ██    ██     ██   ██ ██   ██ ██       
███████ ██    ██    ██    ██    ██     ██████  ██████  ██   ███ 
██   ██ ██    ██    ██    ██    ██     ██   ██ ██      ██    ██ 
██   ██  ██████     ██     ██████      ██   ██ ██       ██████  
                                                                
                                                                
"""))
  
start()

def timer():
    print(fade.purpleblue("starting in 5 seconds"))
    time.sleep(1)
    print(fade.purpleblue("starting in 4 seconds"))
    time.sleep(1)
    print(fade.purpleblue("starting in 3 seconds"))
    time.sleep(1)
    print(fade.purpleblue("starting in 2 seconds"))
    time.sleep(1)
    print(fade.purpleblue("starting in 1 second"))
    os.system("cls")
    start()
timer()


########## FUNCTIONS ##########
def adventure():
    while True:
        time.sleep(18)
        print(Fore.BLUE + "> Adventure has started!")
        pyautogui.moveTo(765, 993, 2)
        pyautogui.click()
        pyautogui.write('RPG heal')
        time.sleep(.6)
        pyautogui.keyDown('enter')
        time.sleep(3)
        pyautogui.write('RPG adv h')
        time.sleep(.5)
        pyautogui.keyDown('enter')
        time.sleep(.8)
        pyautogui.write('RPG heal')
        time.sleep(.5)
        pyautogui.keyDown('enter')
        print(Fore.GREEN + '> Succesfully did rpg-adv and rpg-heal sleeping for 1815 seconds')
        time.sleep(2340)
    

def dynamite():
    while True:
        time.sleep(6)
        print(Fore.GREEN + "> dynamite")
        pyautogui.moveTo(765, 993, 2)
        pyautogui.click()
        pyautogui.write('RPG dynamite')
        time.sleep(.5)
        pyautogui.keyDown('enter')
        print(Fore.GREEN + '> Successfully did dynamite sleeping for 189 seconds')
        time.sleep(189)
        
def farm():
    while True:
        time.sleep(10)
        print(Fore.GREEN + "> farming")
        pyautogui.moveTo(765, 993, 2)
        pyautogui.click()
        pyautogui.write('RPG farm')
        time.sleep(.5)
        pyautogui.keyDown('enter')
        print(Fore.GREEN + '> Succesfully did rpg-farm sleeping for 290 seconds')
        time.sleep(378)
        
def hunts():
    while True:
        time.sleep(.7)
        print(Fore.GREEN + "> hunting together")
        pyautogui.moveTo(765, 993, 2)
        pyautogui.click()
        pyautogui.write('RPG hunt h t')
        time.sleep(.5)
        pyautogui.keyDown('enter')
        print(Fore.GREEN + '> Succesfully did rpg-hunt and heal sleeping for 30 seconds')
        time.sleep(68.3)

########## THREADS ##########

if __name__ == '__main__':
    t1 = threading.Thread(target=adventure)
    t2 = threading.Thread(target=dynamite)
    t3 = threading.Thread(target=farm)
    t4 = threading.Thread(target=hunts)
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # wait for the threads to finish
    t1.join()
    t2.join()
    t3.join()
    t4.join()