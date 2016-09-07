import yaml
import sys
import copy
import random 
from inventory import Inventory
inv =  Inventory()


class Genie(object):
    """docstring for Genie"""
    def __init__(self):
        self.question = []
        self.puzzle_list = []
        with open("data.yml",'r') as puzzle_file:
            self.puzzle_list = yaml.load(puzzle_file)

    def genie_ask(self,a_maze):
        a=a_maze
        user=input("Genie: Are you ready to answer my question? Y/N >  ")
        if user=="y":
            question = random.choice(self.puzzle_list)
            print(question["puzzle"])
            print(question["options"])
            answer=question["answer"]
            user_answer = input("Enter your answer: ")
            if (user_answer==answer):
                print("Correct.")
                self.genie_gift(a)
            else:
                print("Wrong answer")


    def genie_gift(self,a_maze):
        a = random.randrange(6)
        if a == 1:
            print(" Excellent.. I am impressed...")
            print("I will show you the exit")
            b=copy.deepcopy(a_maze)
            for indx, i in enumerate(b):
                for jindx, j in enumerate(i):
                    if j == "P" or j == "E":
                        pass
                    else:
                        b[indx][jindx] = '-'
            for i in b:
                print("\t".join(i))


        elif a == 2:
            print("Great.. I will show you where the Monsters are hidding.")
            b=copy.deepcopy(a_maze)
            for indx, i in enumerate(b):
                for jindx, j in enumerate(i):
                    if j == "P" or j == "M":
                        pass
                    else:
                        b[indx][jindx] = '-'
            for i in b:
                print("\t".join(i))
            
        elif a == 3:
            print("I will give you two extra keys")
            inv.add("keys")
            inv.add("keys")

        elif a == 4:
            print("I will give you two extra weapons")
            inv.add("weapons")
            inv.add("weapons")

        elif a == 5:
            print("I will give you 5 extra moves")
            for x in range(5):
                inv.add("moves")
  
        else:
            print("Sorry. I dont have any gift for you.")
 



