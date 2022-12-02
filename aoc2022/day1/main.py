import os

# Working directory
print(os.getcwd(),'\n')

with open('aoc2022/day1/task.txt','r') as file:
    inputs = [(x) for x in file]


elf_food = []

for inp in inputs:
    if inp == '\n':
        elf_food.append(0)
elf_food.append(0)

sum = 0
i = 0
for inp in inputs:
    if inp != '\n':
        sum += int(inp)
    else:
        elf_food.pop(i)
        elf_food.insert(i, sum)
        i+=1
        sum = 0
elf_food.pop(i)
elf_food.insert(i, sum)   
    
max1 = elf_food[0]
max2 = 0
max3 = 0


for e in elf_food:
    if e > max1:
        max3 = max2
        max2 = max1
        max1 = e
    elif e > max2:
        max3 = max2
        max2 = e
    elif e > max3:
        max3 = e
    
print(max1, max2, max3)
print(max1+max2+max3)