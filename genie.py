import yaml
import sys
import random 
from rooms import Room
from inventory import Inventory

inv =  Inventory()
g_room = Room()

class Genie(object):
    """docstring for Genie"""
    def __init__(self):
        self.question = []
        self.puzzle_list = []
        with open(data,'r') as puzzle_file:
            self.puzzle_list = yaml.load(puzzle_file)

    def genie_ask(self):
        user=input("Genie: Are you ready to answer my question? Y/N >  ")
        if user=="Y":
            question = random.choice(puzzle_list)
            print(question["puzzle"])
            print(question["options"])
            answer=question["answer"]
            user_answer = input("Enter your answer: ")
            if (user_answer==answer):
                print("Correct.")
                self.genie_gift()
            else:
                print("Wrong answer")

    def genie_gift(self):
        a = random.randrange(6)
        if a == 1:
            print(" Excellent.. I am impressed...")
            print("I will show you the exit")
            b=g_room.result()
            for indx, i in enumerate(b):
                for jindx, j in enumerate(i):
                    if j == "P":
                        pass
                    else:
                        b[indx][jindx] = '-'
            for i in b:
                print(" ".join(i))

        elif a == 2:
                print("Great.. I will show you where the Monsters are hidding.")
        elif a == 3:
            print("I will give you two extra keys")
            inv.add("keys")
            inv.add("keys")
        elif a == 4:
            print("I will give you two extra weapons")
            inv.add(weapons=2)
        elif a == 5:
            print("I will give you 5 extra moves")
            inv.add(moves = 5)
        else:
            print("Sorry. I dont have any gift for you.")

