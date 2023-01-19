import numpy as np
import os 

print(os.getcwd())

with open('input.txt', 'r') as file:
    inputs = [x.strip() for x in file]

print(inputs)

# L U D R