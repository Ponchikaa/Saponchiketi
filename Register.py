import os
import time


def register():
    RegName = input("Type your name to register: ")
    RegPass = input("Create Your Password: ")
    if len(RegName) >= 16:
        print("Error Maximum 15 Letters")
        exit()
    if len(RegPass) >= 16:
        print("Error Maximum 15 Password letters")
        exit()
    if len(RegName) <= 15 and len(RegPass) <= 15:
        print("You've been sucssesfully Registered")
register()

