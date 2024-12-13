from functools import cache

file = 'input.txt'

with open(file, 'r') as f:
    data = [[int(y) for y in x.strip().split()] for x in f.readlines() if x.strip() != ''][0]

@cache
def goover(stone, blink):
    if blink == 0:
        return 1

    if stone == 0:
        return  goover(1, blink-1)

    digits = str(stone)
    n = len(digits)
    if n % 2 == 0:
        left = int(digits[:n//2])
        right = int(digits[n//2:])
        
        return goover(left, blink-1) + goover(right, blink-1)

    return goover(2024 * stone, blink-1)


total = 0
for stone in data:
    total += goover(stone, 75)

print(total)
