# Author: Will Hearn
# Class: Python Programming
# Program: Loops
from random import randint
from time import sleep
from sys import platform
from os import system

if platform == "win32":
    clear = "clear"
else:
    clear = "cls"

picture = [
            ["0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0"],
            [" ", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0", " "],
            [" ", " ", "0", " ", " ", " ", " ", " ", " ", " ", "0", " ", " "],
            [" ", " ", " ", "0", " ", " ", " ", " ", " ", "0", " ", " ", " "],
            [" ", " ", " ", " ", "0", " ", " ", " ", "0", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", "0", " ", "0", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", "0", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", "0", " ", "0", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", "0", " ", " ", " ", "0", " ", " ", " ", " "],
            [" ", " ", " ", "0", " ", " ", " ", " ", " ", "0", " ", " ", " "],
            [" ", " ", "0", " ", " ", " ", " ", " ", " ", " ", "0", " ", " "],
            [" ", "0", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0", " "],
            ["0", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "0"],
        ]

def print_structure(img):
    for row in range(13):
        for column in range(len(img)):
            if img[row][column]:
                print(img[row][column], end=" ")
        print()


def coin_flip():
    side = randint(0, 2)
    if side == 0:
        return "Heads"
    else:
        return "Tails"


if __name__ == '__main__':
    while True:
        choice = input("Choose a game!\nPrint Image (1)\nCoin Flip (2)\nQuit (3)\n")
        if choice == "1":
            print_structure(picture)
            sleep(2)
            system(clear)
        elif choice == "2":
            print(coin_flip())
            sleep(2)
            system(clear)
        elif choice == "3":
            exit(0)
        else:
            print("Must enter 1, 2, or 3...")
            sleep(2)
            system(clear)



