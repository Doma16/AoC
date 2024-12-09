file = 'input.txt'

with open(file, 'r') as f:
    data = [int(x) for x in f.read().strip()]

memory = []
id = 0
for i, size in enumerate(data):
    if i % 2 == 0:
        memory.append((size, id))
        id += 1
    else:
        memory.append((size, None))

def concat(i, memory):
    mi = memory[i]
    mii = memory[i+1]
    if mi[1] is None and mii[1]:
        memory = memory[:i] + memory[i+2:]
        memory.insert(i, (mi[0] + mii[0], None))

def move(i, j):
    size_i = memory[i][0]
    size_j, id_j = memory[j]
    left_over = size_j - size_i

    if left_over == 0:
        memory[i], memory[j] = memory[j], memory[i]
    elif left_over < 0:
        memory[j] = (size_j, None)
        memory[i] = (size_j, id_j)
        memory.insert(i+1, (abs(left_over), None))
        #concat(i+1, memory)
    return True


i, j = 0, len(memory) - 1
while i < j:
    while memory[i][1] is not None:
        i += 1

    while memory[j][1] is None:
        j -= 1

    if not(i < j):
        break

    sj, _ = memory[j]
    loc = None
    for k in range(i, j, 1):
        if memory[k][1] is None and memory[k][0] >= sj:
            loc = k
            break

    if loc is not None:
        move(loc, j)
    else:
        j -= 1

def out(memory):
    out = []
    for size, id in memory:
        if id is None:
            out.extend([-1] * size)
        else:
            out.extend([id] * size)
    return out

def checksum(out):
    cs = [idx * id for idx, id in enumerate(out) if id != -1]
    return sum(cs)

output = out(memory)
print(checksum(output))