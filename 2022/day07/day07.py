input_file = '/Users/JHuck/Documents/GitHub/advent-of-code/2022/day07/input.txt'

with open(input_file) as f:
    s = f.readlines()

s = [x.strip().split(' ') for x in s]

class Node(object):
    def __init__(self, data, type, parent, size=0):
        self.data = data
        self.type = type
        self.parent = parent
        self.size = size
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

#Sample Data:
#$ cd /
#$ ls
#dir lhrfs
#193233 mvsjmrtn
#dir nwh
#dir pjsd
#dir qfrrtb
#31987 zzdfcs

cd = []
nl = []


for i in s:
    if i[1] == 'cd':
        if i[2] == '..':
            cd.pop()
        elif i[2] == '/':
            nl.append(Node(i[2],'dir',''))
            cd.append(i[2])
        else:
            cd.append(i[2])
    if i[0] == 'dir':
        for x in nl:
            if x.data == cd[-1]:
                x.add_child(i[1])
        nl.append(Node(i[1],'dir',cd[-1]))
    if i[0].isdigit():
        for x in nl:
            if x.data == cd[-1]:
                x.add_child(i[1])
        nl.append(Node(i[1],'file',cd[-1],i[0])) 

size = []
cl = []

for i in nl:
    if int(i.size) > 0:
        size.append([i.parent,i.size])
    cl.append(i.children)
    for x in cl:
        for x1 in nl:
            x1.data
            x
            if x == x1.data:
                if int(x1.size) > 0:
                    size.append([i.parent,i.size])
                cl.append(x1.children)
                x
                x1
        cl.remove(x)


for i in tt:
    if '4' in
for i in dir_list:
    i.data
    for n in i.children:
        n
        n.data
        size.append(n.size)
        n.data


size = []
dir_list = [r]
for i in dir_list:
    i.data
    dir_list.append(i)
    for n in i.children:
        size.append(n.size)
        n.data

sum(size)
