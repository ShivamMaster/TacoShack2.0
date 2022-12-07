import pyautogui
import time
import random

time.sleep(3)
 
command1 = 0      #control when actual tip, work, and overtime command will run
command2 = 0      #Controls the loop that runs controls when the tip, work, and overtime command will run


while (command2 < 101):
    while (command1 < 1):   
        for line in open("TacoShackCommands.txt", "r"):
            pyautogui.typewrite(line)
            time.sleep(2)
            pyautogui.press("enter")
            pyautogui.press("enter")
        command1 = command1 + 1
    
    command2 = command2 + 1
    time.sleep(300 + random.randint(0,60))
    command1 = 0 
