input_file = '/Users/jhuck/Documents/GitHub/advent-of-code/2022/day07/input.txt'

with open(input_file) as f:
    s = f.readlines()

s = [x.strip().split(' ') for x in s]

r = {'root':{}
}

cd = ['root']

for i in s:
    if i[0] == 'dir':
        r[cd][i0] = {} 
    if i[0].isdigit:
        r[cd][i[1]] = i[0]   
    if i[1] == 'cd':
        cd = i[2]

r = {'root':{
    'a':{
        'file1':11335,
        'file2':1245,
        'b': {
            'file3':1245
        }
    }
}}

r['root']['test'] = 'x'

r 