import re
import os
import math
import numpy as np
print(os.getcwd())

with open('./day6/input.txt','r') as file:
    inputs = [x.strip() for x in file]

time = [ int(x) for x in inputs[0].split(':')[1].split() ]
distance = [ int(x) for x in inputs[1].split(':')[1].split() ]

succ = []
for t, d in zip(time, distance):
    
    t_2 = t**2
    D = math.sqrt(t_2 - 4*d)
    x1 = (t - D) / 2
    x2 = (t + D) / 2

    start = math.floor(x1+1)
    end = math.ceil(x2-1)

    diff = end - start + 1
    succ.append(diff)

print(f'Part 1: prod {np.prod(succ)}')

time2 = "".join([ str(x) for x in time])
distance2 = "".join([ str(x) for x in distance])

t = int(time2)
d = int(distance2)

    
t_2 = t**2
D = math.sqrt(t_2 - 4*d)
x1 = (t - D) / 2
x2 = (t + D) / 2

start = math.floor(x1+1)
end = math.ceil(x2-1)
diff = end - start + 1

print(f'Part 2: total {diff}')