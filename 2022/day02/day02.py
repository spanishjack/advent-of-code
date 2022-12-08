input_file = '/Users/jhuck/Documents/GitHub/advent-of-code/2022/day02/input.txt'

with open(input_file) as f:
    s = f.readlines()

s = [x.strip() for x in s]

# a=rock, b=paper, c=scissors
# x=rock, y=paper, z=scissors
# 6 points win, 3 points draw, 0 points lose
# 1 point rock, 2 points paper, 3 points scissors
# x = lose, y = draw, z = win

def game(a,b):
    if a=='X' and b=='A':
        return(3)
    elif a=='X' and b=='B':
        return(0)
    elif a=='X' and b=='C':
        return(6)
    elif a=='Y' and b=='A':
        return(6)
    elif a=='Y' and b=='B':
        return(3)
    elif a=='Y' and b=='C':
        return(0)
    elif a=='Z' and b=='A':
        return(0)
    elif a=='Z' and b=='B':
        return(6)
    elif a=='Z' and b=='C':
        return(3)

def game2(a,b):
    if a=='X' and b=='A':
        return(3)
    elif a=='X' and b=='B':
        return(1)
    elif a=='X' and b=='C':
        return(2)
    elif a=='Y' and b=='A':
        return(1)
    elif a=='Y' and b=='B':
        return(2)
    elif a=='Y' and b=='C':
        return(3)
    elif a=='Z' and b=='A':
        return(2)
    elif a=='Z' and b=='B':
        return(3)
    elif a=='Z' and b=='C':
        return(1)

def points(x):
    if x=='X':
        return(1)
    elif x=='Y':
        return(2)
    elif x=='Z':
        return(3)

def points2(x):
    if x=='X':
        return(0)
    elif x=='Y':
        return(3)
    elif x=='Z':
        return(6)

t = []
t2 = []

for i in s:
    t.append(game(i[2],i[0]) + points(i[2]))
    t2.append(game2(i[2],i[0]) + points2(i[2]))

sum(t)
sum(t2)
