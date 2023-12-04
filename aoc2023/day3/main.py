import re
import os
import numpy as np
print(os.getcwd())

with open('./day3/input.txt','r') as file:
    inputs = [x.strip() for x in file]


parts = dict()
gear_ratios = []
for hgt, (before, check, after) in enumerate(zip(inputs[0:-2], inputs[1:-1], inputs[2:])):
        
    for i, letter in enumerate(check):
        if not(letter.isalnum() or letter == '.'):

            added = []
            # check up down and curr
            for j in range(i-1, i+1+1):
                
                if check[j].isalnum():
                    num = check[j]
                    if j < i:
                        alt = check[:j] + 'A'
                    else:
                        alt = 'A' + check[j+1:] 
                    pattern = r'\.+'
                    splitted = re.split(pattern, alt)
                    number = [x for x in splitted if x.find('A') != -1][0]
                    number = ''.join([x for x in number if x.isalnum()])
                    fA = number.find('A')
                    delta = len(number[:fA])
                    number = number[:fA] + num + number[fA+1:]
                    parts[(j-delta, hgt)] = int(number)
                    added.append(int(number))
                if before[j].isalnum():
                    num = before[j]
                    alt = before[:j] + 'A' + before[j+1:]
                    pattern = r'\.+'
                    splitted = re.split(pattern, alt)
                    number = [x for x in splitted if x.find('A') != -1][0]
                    number = ''.join([x for x in number if x.isalnum()])
                    fA = number.find('A')
                    delta = len(number[:fA])
                    number = number[:fA] + num + number[fA+1:]
                    parts[(j-delta, hgt-1)] = int(number)
                    added.append(int(number))
                if after[j].isalnum():
                    num = after[j]
                    alt = after[:j] + 'A' + after[j+1:]
                    pattern = r'\.+'
                    splitted = re.split(pattern, alt)
                    number = [x for x in splitted if x.find('A') != -1][0]
                    number = ''.join([x for x in number if x.isalnum()])
                    fA = number.find('A')
                    delta = len(number[:fA])
                    number = number[:fA] + num + number[fA+1:]
                    parts[(j-delta, hgt+1)] = int(number)
                    added.append(int(number))

            added = set(added)
            if letter == '*' and len(added) == 2:
                gear_ratios.append(np.prod(list(set(added))))

'''
line_keys = dict()
for k in parts.keys():
    line_keys.setdefault(k[1], [])
    line_keys[k[1]].append(parts[k])

line_keys = sorted(line_keys.items())
for k, v in line_keys:
    print(f'Line {k}: {v}')
'''

print(f'Part 1: sum is {sum(int(x) for x in parts.values())}')
print(f'Part 2: sum is {sum(gear_ratios)}')
