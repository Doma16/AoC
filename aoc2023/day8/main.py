import os
print(os.getcwd())

with open('./day7/input.txt','r') as file:
    inputs = [x.strip() for x in file]

print(inputs)