input_file = '/Users/jhuck/Documents/GitHub/advent-of-code/2022/day01/input.txt'

with open(input_file) as f:
    s = f.readlines()

s = [x.strip() for x in s]

k  = 0
r = 0
t = []

for i in s:
    if i.isnumeric():
        k  = k  + int(i)
    else:
        if k  > r:
            r = int(k)
        t.append(k)
        k  = 0

#print top value
r
#print sum top 3 values
sum(sorted(t, reverse=True)[:3])