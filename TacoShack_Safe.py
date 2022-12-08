import pyautogui
import time
import random

time.sleep(3)
 
command1 = 0      #control when actual tip, work, and overtime command will run
command2 = 0      #Controls the loop that runs controls when the tip, work, and overtime command will run
command3 = 0      # This will give more Varability as there is more randomness and it will take a random break between the command sequences

while (comand3 < 5):
    while (command2 < random.randint (1,5)):
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
    comand3 = command3 + 1
    time.sleep(random.randint(0,321)) 
