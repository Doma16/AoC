file = 'input.txt'

with open(file, 'r') as f:
    data = [[int(y) for y in x.strip().split()] for x in f.readlines() if x.strip() != ''][0]


dp = {}
def rule(n):
    if n == 0:
        return [1]
    
    if n in dp:
        return dp[n]

    digits = str(n)
    ndigits = len(digits)
    if ndigits % 2 == 0:
        out = [int(digits[:ndigits//2]), int(digits[ndigits//2:])]
        dp[n] = out
        return out

    out = [2024 * n]
    dp[n] = out
    return out

blinks = 25
i = 0
old = data
new = []
while i < blinks:
    for j, el in enumerate(old):
        new.extend(rule(el))
    old = new
    new = []
    i += 1

print(len(old))