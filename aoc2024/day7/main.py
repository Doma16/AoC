import operator

file = 'input.txt'

with open(file, 'r') as f:
    data = [x.strip().split() for x in f.readlines() if x.strip() != '']

Y = [int(x[0][:-1]) for x in data]
X = [[int(y) for y in x[1:]] for x in data]

def concat(a,b):
    return int(str(a) + str(b))

ops = [operator.add, operator.mul, concat]

def accumulate(x, y, i=0, acc=0, op=None, sols=None):
    if i >= len(x):
        sols.append(acc)
        return
    if i == 0:
        acc = x[i]
    else:
        acc = op(acc, x[i])
        if acc > y:
            return

    for op in ops:
        accumulate(x, y, i=i+1, acc=acc, op=op, sols=sols)
    

#part1
cnt = 0
for y, x in zip(Y, X):
    sols = []
    accumulate(x, y, sols=sols)
    if y in sols:
        cnt += y

print(f'part1: {cnt} - k, remove concat op')
print(f'part2: {cnt}')