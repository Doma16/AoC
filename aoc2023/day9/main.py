import os
import math
print(os.getcwd())

with open('./day9/input.txt','r') as file:
    inputs = [x.strip() for x in file]

sequences = [[int(y) for y in x.split()] for x in inputs]

def sub_seq(seq):
    stride = seq[1:] + [seq[0]]
    delta = [ x[1]-x[0] for x in zip(seq, stride)][:-1]
    return delta

def end_test(seq):
    for el in seq:
        if el != 0:
            return False
    return True 

def p1():

    results = []
    for seq in sequences:
        
        last = []
        curr = seq.copy()
        while not end_test(curr):
            last.append(curr[-1])
            curr = sub_seq(curr)

        results.append(sum(last))

    print(f'Part 1: sum {sum(results)}')    

def p2():

    results = []
    for seq in sequences:
        
        first = []
        curr = seq.copy()
        while not end_test(curr):
            first.append(curr[0])
            curr = sub_seq(curr)

        first = [ x if id%2==0 else -x for id, x in enumerate(first) ]
        results.append(sum(first))
    print(f'Part 2: sum {sum(results)}')

if __name__ == '__main__':
    p1()
    p2()