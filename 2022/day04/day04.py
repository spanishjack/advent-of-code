input_file = '/Users/jhuck/Documents/GitHub/advent-of-code/2022/day04/input.txt'

with open(input_file) as f:
    s = f.readlines()

s = [x.strip() for x in s]

t=[]

for i in s:
    x=i.split(',')
    t.append([x[0].split('-'),x[1].split('-')])



# check for fully overlappiing sections
tt = []

for i in t:
    overlap1 = True
    overlap2 = True
    overlap = False
    x_range = list(range(int(i[0][0]),int(i[0][1])+1))
    y_range = list(range(int(i[1][0]),int(i[1][1])+1))

    for y in x_range:
        if y not in y_range:
            overlap1 = False
    for x in y_range:
        if x not in x_range:
            overlap2 = False
    if overlap1 is True or overlap2 is True:
        overlap = True
    tt.append([i[0],i[1],overlap,x_range,y_range])

cnt = 0

for i in tt:
    if i[2] is True:
        cnt+=1
cnt

# check for any overlappiing sections
tt2 = []

for i in t:
    overlap1 = False
    overlap2 = False
    overlap = False
    x_range = list(range(int(i[0][0]),int(i[0][1])+1))
    y_range = list(range(int(i[1][0]),int(i[1][1])+1))

    for y in x_range:
        if y in y_range:
            overlap1 = True
    for x in y_range:
        if x in x_range:
            overlap2 = True
    if overlap1 is True or overlap2 is True:
        overlap = True
    tt2.append([i[0],i[1],overlap,x_range,y_range])

cnt2 = 0

for i in tt2:
    if i[2] is True:
        cnt2+=1
cnt2