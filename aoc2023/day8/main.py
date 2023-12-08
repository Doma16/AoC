import os
import math
print(os.getcwd())

with open('./day8/input.txt','r') as file:
    inputs = file.read()

moves, jumps = inputs.split('\n\n')
moves = moves.strip()

jumps = jumps.strip().split('\n')

# node -> l | r
map = dict()
for jump in jumps:
    node, to = jump.split('=')
    node = node.strip()
    to = to[2:-1]
    to = tuple(to.split(', '))
    map[node] = to

def p1(curr = 'AAA'):
    end = 'ZZZ'

    steps = 0
    while curr != 'ZZZ':
        
        for mov in moves:
            if mov == 'L':
                curr = map[curr][0]
                steps += 1
            elif mov == 'R':
                curr = map[curr][1]
                steps += 1

    print(f'Part 1: steps {steps}')
    return steps

def endtest(currs):
    for curr in currs:
        if curr[-1] != 'Z':
            return False
    return True

def p2():
    
    currs = [ x for x in map.keys() if x[-1] == 'A' ]
    steps_n = [0] * len(currs)

    for idx, curr in enumerate(currs):
        
        steps = 0
        while curr[-1] != 'Z':

            for mov in moves:
                if mov == 'L':
                    curr = map[curr][0]
                    steps += 1
                elif mov == 'R':
                    curr = map[curr][1]
                    steps += 1

        steps_n[idx] = steps
    
    denom = steps_n[0]
    for el in steps_n:
        g_c_d = math.gcd(denom, el)
        denom = denom * el
        denom /= g_c_d
        denom = int(denom)

    print(f'Part 2: steps {denom}')
    return denom

if __name__ == '__main__':
    p1()
    p2()
