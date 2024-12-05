import numpy as np
input_f = 'input.txt'

with open(input_f, 'r') as f:
    data = f.read().strip()


#part1
muls = data.split('mul')[1:]

part1 = 0
for mul in muls:
    left = next((i for i,x in enumerate(mul) if x == '('), None)
    right = next((i for i,x in enumerate(mul) if (x) == ')'), None)

    if right is None or left is None:
        continue

    if right - left < 4 or left != 0:
        continue

    test = mul[left+1:right].replace(' ', 'A')
    
    # file.write(f"mul({test})\n")

    test = test.split(',')
    
    if len(test) != 2:
        continue

    try:
        part1 += np.product([int(x) for x in test])
    except Exception:
        continue

#part2
part2 = 0
enabled = 1
i = 0
n = len(data)
match_dont = 'don\'t()'
match_do = 'do()'
match_mul = 'mul('
while i < n:
    if enabled:
        #dont
        if data[i:i+len(match_dont)] == match_dont:
            enabled = 0
            i += len(match_dont)
            continue
        #mul
        if data[i:i+len(match_mul)] == match_mul:
            i += len(match_mul)
            right = next((i for i,x in enumerate(data[i:i+9]) if (x) == ')'), None)

            if right is None:
                continue

            if right < 3:
                i += right
                continue

            test = data[i:i+right].split(',')
            if len(test) != 2:
                i += right
                continue

            try:
                part2 += np.product([int(x) for x in test])
            except Exception:
                ...
            i += right
            continue
    else:
        #do
        if data[i:i+len(match_do)] == match_do:
            enabled = 1
            i += len(match_do)
            continue

    i+=1

breakpoint()
