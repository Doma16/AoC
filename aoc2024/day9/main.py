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

#part1
def move(i, j):
    size_i = memory[i][0]
    size_j, id_j = memory[j]

    left_over = size_j - size_i
    # equal
    if left_over == 0:
        memory[i], memory[j] = memory[j], memory[i]
    elif left_over > 0:
        memory[i] = (size_i, id_j)
        memory[j] = (left_over, id_j)
        memory.insert(j+1, (size_i, None))
    else:
        memory[j] = (size_j, None)
        memory[i] = (size_j, id_j)
        memory.insert(i+1, (abs(left_over), None))

i, j = 0, len(memory) - 1
while i < j:

    while memory[i][1] is not None:
        i += 1

    while memory[j][1] is None:
        j -= 1

    if not(i < j):
        break
    move(i, j)

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

print(checksum(out(memory)))