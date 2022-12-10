input_file = '/Users/jhuck/Documents/GitHub/advent-of-code/2022/day03/input.txt'

with open(input_file) as f:
    s = f.readlines()

s = [x.strip() for x in s]

z = []

for i in s:
    z.append([i,i[:int(len(i)/2)],i[int(len(i)/2):]])

t = []

for i in z:
    x = ''
    for y in i[1]:
        if y in i[2]:
            if y not in x:
                x+=y
    t.append([i,x])

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
# Use ord unicode index to get alphabet position
lc_ord_index = 96
uc_ord_index = 38

l = []

for i in t:
    print(i)
    for x in i[1]:
        print(x)
        if x == x.upper():
            l.append(ord(x) - uc_ord_index)
        else:
            l.append(ord(x) - lc_ord_index)

sum(l)

# part 2, for groups of 3
tt = []
tt2 = []

for idx, i in enumerate(z):
    if idx % 3 == 0 and idx > 0:
        tt2.append(tt)
        tt = []
    tt.append(i[0])

    if idx+1 == len(z):
        tt2.append(tt)

t2 = []

for i in tt2:
    x = ''
    for y in i[0]:
        if y in i[1] and y in i[2]:
            if y not in x:
                x+=y
    t2.append([i,x])

l2 = []

for i in t2:
    for x in i[1]:
        if x == x.upper():
            l2.append(ord(x) - uc_ord_index)
        else:
            l2.append(ord(x) - lc_ord_index)

sum(l2)