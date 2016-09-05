import math
import random
from random import shuffle
from inventory import Inventory
import genie
inv = Inventory()
genie1= Genie()

class Room():
    """docstring for ClassName"""
    def __init__(self, level=1):
        self.level = level+1

    def maze_size(self):
        mazesize = []
        for i in range(self.level):
            a=["-"]*(self.level)
            mazesize.append(a)
        return mazesize

    
    def maze_setup(self):
        a=self.maze_size()

        temp=[]
        for i in a:
            for j in i:
                temp.append(j)

        if (self.level>2):
            monster_numbers =self.level
        elif(self.level == 2):
            monster_numbers =1
        else:
            monster_numbers=0
        l=["P","E"]
        for m in range(monster_numbers):
            l.append("M")

        for i in range(len(l)):
            temp[i]=l[i]

        print(temp)
        print(shuffle(temp))
        x=[]
        for i in range(self.level):
            x=temp[:self.level]
            del temp[:self.level]
            a.append(x)
        return a

    
    def result_maze(self,a_maze):
        a = a_maze
        return a

    def display_maze(self,a_maze):
        b = a_maze
        print ("Your playing maze is: ")
        for indx, i in enumerate(b):
            for jindx, j in enumerate(i):
                if j == "P":
                    pass
                else:
                    b[indx][jindx] = '-'
        for i in b:
            print(" ".join(i))


    def move_up(self,a_maze):
        a=a_maze
        try:
            for indx, i in enumerate(a):
                for jindx, j in enumerate(i):
                    if a[indx-1][jindx1]=="P":
                        a[indx][jindx] = "-"
                        a[indx-1][jindx] = "P"
                        break

                    elif a[indx-1][jindx]=="E":
                        print("You got into the room with exit door.")
                        print("Use your key to exit the maze.")
                        while True:
                            k=input("> ")
                            if k == "k":
                                c = inv.check("keys")
                                if c:
                                    print("You got into exit.\n Level up.")
                                    inv.remove("keys")
                                    break
                                else:
                                    print("You dont have keys to exit. Try life-line.")
                            elif k == "g":
                                c = inv.check("life_line")
                                if c:
                                    print("You got a life line.")
                                    genie1.genie_ask()
                                    inv.remove("life_line")
                                else:
                                    print("You dont have life-line.")
                            elif k == "w":
                                c= inv.check("weapons")
                                if c: 
                                    print("You have wasted your weapon.")
                                    inv.remove("weapons")
                                else:
                                    print("You dont have weapons")
                            elif k =="x":
                                print("You lose. Exiting the game.")
                                sys.exit()

                    elif a[indx-1][jindx] =="M":
                        print("You got into Monster room. Use your weapon to kill the monster.")
                        while True:
                            k=input("> ")
                            if k== "k":
                                c = inv.check("keys")
                                if c:
                                    print("You wasted your key.")
                                    inv.remove("keys")
                                else:
                                    print("You dont have keys. Try life-line.")
                            elif k== "g":
                                c = inv.check("life_line")
                                if c:
                                    print("You got a life line.")
                                    genie1.genie_ask()
                                    inv.remove("life_line")
                                else:
                                    print("You dont have life-line.")
                            elif k== "w":
                                c= inv.check("weapons")
                                if c: 
                                    print("You killed the monster")
                                    inv.remove("weapons")
                                    break
                                else:
                                    print("You dont have weapons. You lose.")
                                    if inv.check("life_line"):
                                        print("Try life line.")
                                        genie1.genie_ask()
                                    else:
                                        print("You lose.")
                                        sys.exit()
                            elif k=="x":
                                print("You lose. Exiting the game.")
                                sys.exit()
                    
            inv.remove("moves")
            return a
        except IndexError:
            print("Oops! Cannot move out of the Maze. Move in some other direction")
            return a
    def move_down(self,a_maze):
        a=a_maze
        try:
            for indx, i in enumerate(a):
                for jindx, j in enumerate(i):
                    if a[indx+1][jindx1]=="P":
                        a[indx][jindx] = "-"
                        a[indx+1][jindx] = "P"
                        break

                    elif a[indx+1][jindx]=="E":
                        print("You got into the room with exit door.")
                        print("Use your key to exit the maze.")
                        while True:
                            k=input("> ")
                            if k == "k":
                                c = inv.check("keys")
                                if c:
                                    print("You got into exit.\n Level up.")
                                    inv.remove("keys")
                                    break
                                else:
                                    print("You dont have keys to exit. Try life-line.")
                            elif k == "g":
                                c = inv.check("life_line")
                                if c:
                                    print("You got a life line.")
                                    genie1.genie_ask()
                                    inv.remove("life_line")
                                else:
                                    print("You dont have life-line.")
                            elif k == "w":
                                c= inv.check("weapons")
                                if c: 
                                    print("You have wasted your weapon.")
                                    inv.remove("weapons")
                                else:
                                    print("You dont have weapons")
                            elif k =="x":
                                print("You lose. Exiting the game.")
                                sys.exit()

                    elif a[indx+1][jindx] =="M":
                        print("You got into Monster room. Use your weapon to kill the monster.")
                        while True:
                            k=input("> ")
                            if k == "k":
                                c = inv.check("keys")
                                if c:
                                    print("You wasted your key.")
                                    inv.remove("keys")
                                else:
                                    print("You dont have keys. Try life-line.")
                            elif k == "g":
                                c = inv.check("life_line")
                                if c:
                                    print("You got a life line.")
                                    genie1.genie_ask()
                                    inv.remove("life_line")
                                else:
                                    print("You dont have life-line.")
                            elif k == "w":
                                c= inv.check("weapons")
                                if c: 
                                    print("You killed the monster")
                                    inv.remove("weapons")
                                    break
                                else:
                                    print("You dont have weapons. You lose.")
                                    if inv.check("life_line"):
                                        print("Try life line.")
                                        genie1.genie_ask()
                                    else:
                                        print("You lose.")
                                        sys.exit()
                            elif k =="x":
                                print("You lose. Exiting the game.")
                                sys.exit()
                    
            inv.remove("moves")
            return a
        except IndexError:
            print("Oops! Cannot move out of the Maze. Move in some other direction")
            return a
    def move_left(self,a_maze):
        a=a_maze
        try:
            for indx, i in enumerate(a):
                for jindx, j in enumerate(i):
                    if a[indx][jindx-1]=="P":
                        a[indx][jindx] = "-"
                        a[indx][jindx-1] = "P"
                        break

                    elif a[indx][jindx-1]=="E":
                        print("You got into the room with exit door.")
                        print("Use your key to exit the maze.")
                        while True:
                            k=input("> ")
                            if k == "k":
                                c = inv.check("keys")
                                if c:
                                    print("You got into exit.\n Level up.")
                                    inv.remove("keys")
                                    break
                                else:
                                    print("You dont have keys to exit. Try life-line.")
                            elif k == "g":
                                c = inv.check("life_line")
                                if c:
                                    print("You got a life line.")
                                    genie1.genie_ask()
                                    inv.remove("life_line")
                                else:
                                    print("You dont have life-line.")
                            elif k == "w":
                                c= inv.check("weapons")
                                if c: 
                                    print("You have wasted your weapon.")
                                    inv.remove("weapons")
                                else:
                                    print("You dont have weapons")
                            elif k =="x":
                                print("You lose. Exiting the game.")
                                sys.exit()

                    elif a[indx][jindx-1] =="M":
                        print("You got into Monster room. Use your weapon to kill the monster.")
                        while True:
                            k=input("> ")
                            if k == "k":
                                c = inv.check("keys")
                                if c:
                                    print("You wasted your key.")
                                    inv.remove("keys")
                                else:
                                    print("You dont have keys. Try life-line.")
                            elif k == "g":
                                c = inv.check("life_line")
                                if c:
                                    print("You got a life line.")
                                    genie1.genie_ask()
                                    inv.remove("life_line")
                                else:
                                    print("You dont have life-line.")
                            elif k == "w":
                                c= inv.check("weapons")
                                if c: 
                                    print("You killed the monster")
                                    inv.remove("weapons")
                                    break
                                else:
                                    print("You dont have weapons. You lose.")
                                    if inv.check("life_line"):
                                        print("Try life line.")
                                        genie1.genie_ask()
                                    else:
                                        print("You lose.")
                                        sys.exit()
                            elif k =="x":
                                print("You lose. Exiting the game.")
                                sys.exit()
                    
            inv.remove("moves")
            return a
        except IndexError:
            print("Oops! Cannot move out of the Maze. Move in some other direction")
            return a
    def move_right(self,a_maze):
        a=a_maze
        try:
            for indx, i in enumerate(a):
                for jindx, j in enumerate(i):
                    if a[indx][jindx+1]=="P":
                        a[indx][jindx] = "-"
                        a[indx][jindx+1] = "P"
                        break

                    elif a[indx][jindx+1]=="E":
                        print("You got into the room with exit door.")
                        print("Use your key to exit the maze.")
                        while True:
                            k=input("> ")
                            if k == "k":
                                c = inv.check("keys")
                                if c:
                                    print("You got into exit.\n Level up.")
                                    inv.remove("keys")
                                    break
                                else:
                                    print("You dont have keys to exit. Try life-line.")
                            elif k == "g":
                                c = inv.check("life_line")
                                if c:
                                    print("You got a life line.")
                                    genie1.genie_ask()
                                    inv.remove("life_line")
                                else:
                                    print("You dont have life-line.")
                            elif k == "w":
                                c= inv.check("weapons")
                                if c: 
                                    print("You have wasted your weapon.")
                                    inv.remove("weapons")
                                else:
                                    print("You dont have weapons")
                            elif k =="x":
                                print("You lose. Exiting the game.")
                                sys.exit()

                    elif a[indx][jindx+1] =="M":
                        print("You got into Monster room. Use your weapon to kill the monster.")
                        while True:
                            k=input("> ")
                            if k == "k":
                                c = inv.check("keys")
                                if c:
                                    print("You wasted your key.")
                                    inv.remove("keys")
                                else:
                                    print("You dont have keys. Try life-line.")
                            elif k == "g":
                                c = inv.check("life_line")
                                if c:
                                    print("You got a life line.")
                                    genie1.genie_ask()
                                    inv.remove("life_line")
                                else:
                                    print("You dont have life-line.")
                            elif k == "w":
                                c= inv.check("weapons")
                                if c: 
                                    print("You killed the monster")
                                    inv.remove("weapons")
                                    break
                                else:
                                    print("You dont have weapons. You lose.")
                                    if inv.check("life_line"):
                                        print("Try life line.")
                                        genie1.genie_ask()
                                    else:
                                        print("You lose.")
                                        sys.exit()
                            elif k =="x":
                                print("You lose. Exiting the game.")
                                sys.exit()
                    
            inv.remove("moves")
            return a
        except IndexError:
            print("Oops! Cannot move out of the Maze. Move in some other direction")
            return a
        

    def call_genie(self):
        pass

