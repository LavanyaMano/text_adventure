import math
import random
from random import shuffle
from inventory import Inventory
from genie import Genie
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
        y=[]
        for i in range(self.level):
            x= temp[:self.level]
            del temp[:self.level]
            y.append(x)
        return y

    
    def result_maze(self,a_maze):
        a = a_maze
        for i in a:
            print("\t".join(i))


    def display_maze(self,dis_maze):
        b = dis_maze
        print ("Your playing maze is: ")
        for indx, i in enumerate(b):
            for jindx, j in enumerate(i):
                if j == "P":
                    pass
                else:
                    b[indx][jindx] = '-'
        for x in b:
            print("\t".join(x))

    def key(self):
        print("You got into the room with exit door.")
        print("Use your key to exit the maze.")
        while True:
            k=input("Enter your choice: ")
            if k == "k":
                c = inv.check("keys")
                if c:
                    print("You got into exit.")
                    inv.remove("keys")
                    inv.add("score")
                    return True
                else:
                    print("You dont have keys to exit. Try life-line.")
            elif k == "g":
                c = inv.check("life_line")
                if c:
                    print("You got a life line.")
                    genie1.genie_ask(a)
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
    def monster(self):
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
                    genie1.genie_ask(a)
                    inv.remove("life_line")
                else:
                    print("You dont have life-line.")
            elif k== "w":
                c= inv.check("weapons")
                if c: 
                    print("You killed the monster")
                    inv.remove("weapons")
                    inv.add("score")
                    break
                else:
                    print("You dont have weapons. You lose.")
                    if inv.check("life_line"):
                        print("Try life line.")
                        genie1.genie_ask(a)
                    else:
                        print("You lose.")
                        sys.exit()
            elif k=="x":
                print("You lose. Exiting the game.")
                sys.exit()

    def move(self,a_maze,side):
        a=a_maze
        try:
            for indx, i in enumerate(a):
                for jindx, j in enumerate(i):
                    if (side == "r"):
                        if j == "P" :
                            if a[indx][jindx+1]=="E":
                                self.key()
                                inv.remove("moves")
                                return a,True
                            elif a[indx][jindx+1] =="M":
                                a[indx][jindx+1] =="P"
                                self.monster()
                                inv.remove("moves")
                                return a,False
                            elif a[indx][jindx+1] == "-":
                                a[indx][jindx] = "-"
                                a[indx][jindx+1] = "P"
                                inv.remove("moves")
                                return a,False
                    elif(side == "l"):
                        if j == "P" :
                            if (jindx-1 <0):
                                raise IndexError
                            elif a[indx][jindx-1]=="E":
                                self.key()
                                inv.remove("moves")
                                return a,True
                            elif a[indx][jindx-1] =="M":
                                self.monster()
                                a[indx][jindx-1] =="P"
                                inv.remove("moves")
                                return a,False
                            elif a[indx][jindx-1] == "-":
                                a[indx][jindx] = "-"
                                a[indx][jindx-1] = "P"
                                inv.remove("moves")
                                return a,False
                    elif(side == "u"):
                        if j == "P" :
                            if (jindx-1 <0):
                                raise IndexError
                            elif a[indx-1][jindx]=="E":
                                self.key()
                                inv.remove("moves")
                                return a,True
                            elif a[indx-1][jindx] =="M":
                                a[indx-1][jindx] = "P"
                                self.monster()
                                inv.remove("moves")
                                return a,False
                            elif a[indx-1][jindx] == "-":
                                a[indx][jindx] = "-"
                                a[indx-1][jindx] = "P"
                                inv.remove("moves")
                                return a,False
                    elif(side == "d"):
                        if j == "P" :
                            print(jindx)
                            if a[indx+1][jindx]=="E":
                                self.key()
                                inv.remove("moves")
                                return a,True
                            elif a[indx+1][jindx] =="M":
                                a[indx+1][jindx] =="P"
                                self.monster()
                                inv.remove("moves")
                                return a,False
                            elif a[indx+1][jindx] == "-":
                                a[indx][jindx] = "-"
                                a[indx+1][jindx] = "P"
                                inv.remove("moves")
                                return a,False
        except IndexError as name:
            print("#"*33)
            print(type(name))
            print(name.args)
            print(name)

            print("Oops! Cannot move out of the Maze. Move in some other direction")
            return a


