import random
import time
import os


def choose():
    Number = random.randint(1, 100)
    print(Number)
    print("Type random number from 1 to 100")
    inp = input(":")
    if inp == Number:
        print("NICE JOB YOU WON 2 PONCHIKIS")
    else:
        print("NOPE :(")
        print("The Number was ", Number)
choose()