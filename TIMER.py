import time
import os
import random

def Timer(Time):
    for i in range(Time):
        Time -= 1
        time.sleep(1)
        os.system('cls')
        print(Time)
        while Time == 0:
            os.system('cls')
            print("!TIME ENDED!")
            exit()

Timer(int(input("Set Timer: ")))