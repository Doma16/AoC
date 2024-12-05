input_f = 'input.txt'

with open(input_f, 'r') as f:
    data = [ [ int(y) for y in x.strip().split() ] for x in f.readlines() if x.strip() != '' ]
    

#part1
lower = 1
upper = 3

diff = [ [ (f-s) for f,s in zip(x[:-1], x[1:]) ] for x in data] 
bounded = [ all(abs(y) >= lower and abs(y) <= upper for y in x) for x in diff ]

def strict_f(diffs):
    f1 = [(x > 0) for x in diffs]
    f2 = [not(x > 0) for x in diffs]

    s1 = sum(f1)
    s2 = sum(f2)

    if s1 > s2:
        return f1
    else:
        return f2
    
for idx, el in enumerate(diff):
    flag = all(strict_f(el))
    bounded[idx] = bounded[idx] and flag

total = sum(bounded)

def diffs(lvls):
    return [x-y for x,y in zip(lvls[:-1], lvls[1:])]

def bound(diffs, lower=lower, upper=upper):
    return [abs(x) >= lower and abs(x) <= upper for x in diffs]


#part2

part2 = 0
for idx, (row) in enumerate(data):
    diff = diffs(row)
    dst = bound(diff)
    flag = all(dst)
    strct = strict_f(diff)
    flag_strct = all(strct)

    if not flag or not flag_strct:
        idy = next((i for i,x in enumerate(dst) if not x), None)
        idy2 = next((i for i,x in enumerate(strct) if not x), None)

        if idy is not None and idy2 is not None:
            idy = min(idy, idy2)

        if idy is None:
            idy = idy2

        row1 = row[:idy] + row[idy+1:]
        row2 = row[:idy+1] + row[idy+2:]

        diff1 = diffs(row1)
        dst1 = bound(diff1)
        flag1 = all(dst1)
        strct1 = strict_f(diff1)
        flag1_strct = all(strct1)

        if flag1 and flag1_strct:
            part2 += 1
            continue

        diff2 = diffs(row2)
        dst2 = bound(diff2)
        flag2 = all(dst2)
        strct2 = strict_f(diff2)
        flag2_strct = all(strct2)

        if flag2 and flag2_strct:
            part2 += 1
            continue
        
        print(row)
        continue
    part2 += 1

breakpoint()