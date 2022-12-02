import numpy as np

inputs = None
with open('./aoc2022/day2/task.txt','r') as file:
    inputs = [x.strip() for x in file]

def aOut(c):
    if c == "A":
        return 1
    elif c == "B":
        return 2
    elif c == "C":
        return 3

def transformXs(x,a):
    a1 = aOut(a)
    if x == "Y":
        return a
    elif x == "X":
        a1 = (a1 - 1 + 3) % 3
        if a1 == 0:
            a1 = 3
        if a1 == 1:
            return "A"
        elif a1 == 2:
            return "B"
        elif a1 == 3:
            return "C"
    elif x == "Z":
        a1 = (a1 + 1) % 3
        if a1 == 0:
            a1 = 3
        if a1 == 1:
            return "A"
        elif a1 == 2:
            return "B"
        elif a1 == 3:
            return "C"

def winner(x,y):
    if x == y:
        return 0
    elif x == 3 and y == 1:
        return -1
    elif x == 1 and y == 3:
        return 1
    elif x < y:
        return -1
    elif x > y:
        return 1

score = 0

for i in inputs:
    a,x = i.split(" ")
    p1 = aOut(a)
    x = transformXs(x,a)
    p2 = aOut(x)
    wins = winner(p2,p1)
    score += p2
    if wins == 1:
        score += 6
    elif wins == 0:
        score += 3
    
print(score)
