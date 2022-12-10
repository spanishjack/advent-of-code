
# starting positions
#
#    [V] [G]             [H]        
#[Z] [H] [Z]         [T] [S]        
#[P] [D] [F]         [B] [V] [Q]    
#[B] [M] [V] [N]     [F] [D] [N]    
#[Q] [Q] [D] [F]     [Z] [Z] [P] [M]
#[M] [Z] [R] [D] [Q] [V] [T] [F] [R]
#[D] [L] [H] [G] [F] [Q] [M] [G] [W]
#[N] [C] [Q] [H] [N] [D] [Q] [M] [B]
# 1   2   3   4   5   6   7   8   9 

c1 = ['N','D','M','Q','B','P','Z']
c2 = ['C','L','Z','Q','M','D','H','V']
c3 = ['Q','H','R','D','V','F','Z','G']
c4 = ['H','G','D','F','N']
c5 = ['N','F','Q']
c6 = ['D','Q','V','Z','F','B','T']
c7 = ['Q','M','T','Z','D','V','S','H']
c8 = ['M','G','F','P','N','Q']
c9 = ['B','W','R','M']

cc = {
    '1':c1,
    '2':c2,
    '3':c3,
    '4':c4,
    '5':c5,
    '6':c6,
    '7':c7,
    '8':c8,
    '9':c9
}

# readfile from row 11 for data
input_file = '/Users/jhuck/Documents/GitHub/advent-of-code/2022/day05/input.txt'

with open(input_file) as f:
    s = f.readlines()[10:]

s = [x.strip().split(' ') for x in s]

# sample: ['move', '3', 'from', '2', 'to', '5']
for i in s:
    for x in range(int(i[1])):
        t = cc[str(i[3])].pop()
        cc[str(i[5])].append(t)

o = ''
for i in cc:
    o+=cc[i][-1]
o

# part two
c1 = ['N','D','M','Q','B','P','Z']
c2 = ['C','L','Z','Q','M','D','H','V']
c3 = ['Q','H','R','D','V','F','Z','G']
c4 = ['H','G','D','F','N']
c5 = ['N','F','Q']
c6 = ['D','Q','V','Z','F','B','T']
c7 = ['Q','M','T','Z','D','V','S','H']
c8 = ['M','G','F','P','N','Q']
c9 = ['B','W','R','M']

cc = {
    '1':c1,
    '2':c2,
    '3':c3,
    '4':c4,
    '5':c5,
    '6':c6,
    '7':c7,
    '8':c8,
    '9':c9
}

# readfile from row 11 for data
input_file = '/Users/jhuck/Documents/GitHub/advent-of-code/2022/day05/input.txt'

with open(input_file) as f:
    s = f.readlines()[10:]

s = [x.strip().split(' ') for x in s]

for i in s:
    e = []
    for x in range(int(i[1])):
        t = cc[str(i[3])].pop()
        e.append(t)
    
    e.reverse()
    for m in e:
        cc[str(i[5])].append(m)

o = ''
for i in cc:
    o+=cc[i][-1]
o
