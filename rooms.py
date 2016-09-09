import math
import sys
import random
import copy
import os
from random import shuffle
from inventory import my_inventory
from genie import Genie
genie1= Genie()

class Room():
    """creating maze class"""
    def __init__(self, level=1):
        self.level = level+1

    """creating maze size as per the level"""
    def maze_size(self):
        mazesize = []
        for i in range(self.level):
            a=["-"]*(self.level)
            mazesize.append(a)
        return mazesize

    """creating maze with P(player),E(exit),M(monster)"""
    def maze_setup(self):
        a=self.maze_size()

        temp=[] # getting temperory list and converting maze array to list.
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

        shuffle(temp)
        y=[]
        for i in range(self.level):
            x= temp[:self.level]
            del temp[:self.level]
            y.append(x)
        return y

    
    def result_maze(self,a_maze): # shows maze with P,E,M positions
        a = a_maze
        for i in a:
            print("\t".join(i))


    def display_maze(self,dis_maze): # shows maze with only P position and hiding E,Ms.
        b = copy.deepcopy(dis_maze)
        print ("Your playing maze is: ")
        for indx, i in enumerate(b):
            for jindx, j in enumerate(i):
                if j == "P":
                    pass
                else:
                    b[indx][jindx] = '-'

        for x in b:
            print("\033[3;32;44m "+"\t".join(x)+"\033[m ")


    def key(self,a):
        print("\033[3;37;45m You got into the room with exit door.\033[m")
        print("Use your key to exit the maze.")
        while True:
            print("k - keys\tw -weapons\tg -lifeline\t x - exit")
            k=input("Enter your choice(use key): ")
            if k == "k":
                c = my_inventory.check("keys")
                if c:
                    print("You got into exit.")
                    my_inventory.remove("keys")
                    my_inventory.add("score")
                    return True
                elif my_inventory.check("life_line"):
                    print("You dont have keys to exit. Try life-line.")
                else:
                    print("You lose.\n Existing the game")
                    sys.exit()
            elif k == "g":
                c = my_inventory.check("life_line")
                if c:
                    os.system("clear")
                    print("You got a life line.")
                    genie1.genie_ask(a)
                    my_inventory.remove("life_line")
                else:
                    print("You dont have life-line.")
            elif k == "w":
                c= my_inventory.check("weapons")
                if c: 
                    print("You have wasted your weapon.")
                    my_inventory.remove("weapons")
                else:
                    print("You dont have weapons")
            elif k =="x":
                print("You lose. Exiting the game.")
                sys.exit()
    def monster(self,temp_maze):
        a= copy.deepcopy(temp_maze)
        print("\033[3;33;41m You got into Monster room. Use your weapon to kill the monster.\033[m")
        while True:
            print("k - keys\tw -weapons\tg -lifeline\n x - exit")
            k=input("Enter yours choice(use weapon): ")
            if k== "k":
                c = my_inventory.check("keys")
                if c:
                    print("You wasted your key.")
                    my_inventory.remove("keys")
                else:
                    print("You dont have keys. Try life-line.")
            elif k== "g":
                c = my_inventory.check("life_line")
                if c:
                    os.system("clear")
                    print("You got a life line.")
                    genie1.genie_ask(a)
                    my_inventory.remove("life_line")
                else:
                    print("You dont have life-line.")
            elif k== "w":
                c= my_inventory.check("weapons")
                if c: 
                    print("You killed the monster")
                    my_inventory.remove("weapons")
                    my_inventory.add("score")
                    break
                else:
                    if my_inventory.check("life_line")>0:
                        print("Try life line.")
                        genie1.genie_ask(a)
                    else:
                        print("You lose.")
                        print  ("___   __   _  _  ____     __   _  _  ____  ____ ")
                        print ("/ __) / _\ ( \/ )(  __)   /  \ / )( \(  __)(  _ \\")
                        print("( (_ \/    \/ \/ \ ) _)   (  O )\ \/ / ) _)  )   /")
                        print ("\___/\_/\_/\_)(_/(____)   \__/  \__/ (____)(__\_)")
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
                                self.key(a)
                                a[indx][jindx+1] ="P"
                                my_inventory.remove("moves")
                                my_inventory.remove("moves")
                                return a,True
                            elif a[indx][jindx+1] =="M":
                                self.monster(a)
                                a[indx][jindx] = "-"
                                a[indx][jindx+1] ="P"
                                my_inventory.remove("moves")
                                return a,False
                            elif a[indx][jindx+1] == "-":
                                a[indx][jindx] = "-"
                                a[indx][jindx+1] = "P"
                                my_inventory.remove("moves")
                                return a,False
                    elif(side == "l"):
                        if j == "P" :
                            if (jindx-1 <0):
                                raise IndexError
                            elif a[indx][jindx-1]=="E":
                                self.key(a)
                                a[indx][jindx] = "-"
                                a[indx][jindx-1] ="P"
                                my_inventory.remove("moves")
                                return a,True
                            elif a[indx][jindx-1] =="M":
                                self.monster(a)
                                a[indx][jindx] = "-"
                                a[indx][jindx-1] ="P"
                                my_inventory.remove("moves")
                                return a,False
                            elif a[indx][jindx-1] == "-":
                                a[indx][jindx] = "-"
                                a[indx][jindx-1] = "P"
                                my_inventory.remove("moves")
                                return a,False
                    elif(side == "u"):
                        if j == "P" :
                            if (indx-1 <0):
                                raise IndexError
                            elif a[indx-1][jindx]=="E":
                                self.key(a)
                                a[indx][jindx] = "-"
                                a[indx-1][jindx] = "P"
                                my_inventory.remove("moves")
                                return a,True
                            elif a[indx-1][jindx] =="M":
                                self.monster(a)
                                a[indx][jindx] = "-"
                                a[indx-1][jindx] = "P"
                                my_inventory.remove("moves")
                                return a,False
                            elif a[indx-1][jindx] == "-":
                                a[indx][jindx] = "-"
                                a[indx-1][jindx] = "P"
                                my_inventory.remove("moves")
                                return a,False
                    elif side == "d":
                        if j == "P" :
                            if a[indx+1][jindx]=="E":
                                self.key(a)
                                a[indx][jindx] = "-"
                                a[indx+1][jindx] ="P"
                                my_inventory.remove("moves")
                                return a,True
                            elif a[indx+1][jindx] =="M":
                                self.monster(a)
                                a[indx][jindx] = "-"
                                a[indx+1][jindx] ="P"
                                my_inventory.remove("moves")
                                return a,False
                            elif a[indx+1][jindx] == "-":
                                a[indx][jindx] = "-"
                                a[indx+1][jindx] = "P"
                                my_inventory.remove("moves")
                                return a,False
        except IndexError as name:
            print("Oops! Cannot move out of the Maze. Move in some other direction")
            return a,False


