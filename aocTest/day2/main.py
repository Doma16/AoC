import os

print(os.getcwd())

with open('aocTest/day2/task.txt','r') as file:
    inputs = [x.strip() for x in file]


depth = 0
distance = 0
aim = 0

for el in inputs:
    cmd, val =  el.split(' ')
    val = int(val)
    if (cmd == 'forward'):
        distance += val
        depth += aim * val
    elif cmd == 'down':
        aim += val
    else:
        aim -= val

print(depth*distance)
