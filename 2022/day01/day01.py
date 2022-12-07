with open('./2022/day01/input.txt') as f:
    s = f.readlines()

s = [x.strip() for x in s]

k  = 0
r = 0

for i in s:
    if i.isnumeric():
        k  = k  + int(i)
    else:
        if k  > r:
            r = int(k)
        k  = 0
r