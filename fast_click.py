import pyautogui
import random
import time
import keyboard


def click():
    pyautogui.click()

    #time.sleep(random.uniform(0.001, 0.0001))
    time.sleep(0.1)
    
    pyautogui.click()



def loop():
    while True:
        if keyboard.is_pressed("r"):
            while keyboard.is_pressed("q") == False:
                click()
            break
    loop()

loop()
