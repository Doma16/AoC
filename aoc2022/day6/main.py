import numpy as np

with open('./aoc2022/day6/task.txt','r') as file:
    inputs = [x.strip() for x in file] 

buffer = inputs[0]

l = list(buffer)

i = 0
length = 14
while( i < (len(buffer)-3)):
    ll = []
    for j in range(length):
        ll.append(buffer[i+j])

    s = { e for e in ll }
    if len(s) == length:
        break
    i+=1
    
print(i+length)