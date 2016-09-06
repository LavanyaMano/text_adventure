
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

    x=[]
    for i in range(self.level):
        x=temp[:self.level]
        del temp[:self.level]
        a.append(x)
    return a
