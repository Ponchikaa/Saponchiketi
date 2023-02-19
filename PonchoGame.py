import time
import random
import os

chall1 = "Do 5 Push ups"
chall2 = "Drink water"
chall3 = "Scream"
chall4 = "eat something"
chall5 = "KILL NIGGERS"

List_of_Chall = [chall1, chall2, chall3, chall4, chall5]

def Timer_chall():
    Time1 = int(5)
    Time2 = int(10)
    rand_Chall = random.choice(List_of_Chall)
    if rand_Chall == chall2 or rand_Chall == chall1:
        for i in range(5):
            time.sleep(1)
            os.system('cls')
            Time2 -= 1
            print(rand_Chall + " in " + str(Time2) + "Sec")
            while Time1 == 0:
                os.system('cls')
                print("TIME IS UP")
                exit()
    else:
        for i in range(5):
            time.sleep(1)
            os.system('cls')
            Time1 -= 1
            print(rand_Chall + " in " + str(Time1) + "Secs")
            while Time1 == 0:
                os.system('cls')
                print("TIME IS UP")
                exit()

Timer_chall()