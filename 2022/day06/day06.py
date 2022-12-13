#examples
#bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
#nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
#nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
#zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11
input_file = '/Users/jhuck/Documents/GitHub/advent-of-code/2022/day06/input.txt'

with open(input_file) as f:
    s = f.readlines()

s = [x.strip().split(' ') for x in s]
x = s[0]
x1 = ''.join(filter(str.isalnum, str(x)))

t1 = []
for xdi, i in enumerate(x1):
    if len(t1) > 3:
        t1.pop(0)
    t1.append(i)
    
    if len(t1) > 3:
        if t1 == list(dict.fromkeys(t1)):
            break
xdi+1

#part 2

#examples
#mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
#bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
#nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
#nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
#zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

t1 = []
for xdi, i in enumerate(x1):
    if len(t1) > 13:
        t1.pop(0)
    t1.append(i)
    
    if len(t1) > 13:
        if t1 == list(dict.fromkeys(t1)):
            break
xdi+1