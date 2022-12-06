with open("input5.txt", "r") as f:
    data = f.readlines()

def movement_line(data):
    row = 0
    for d in data:
        if 'move' in d:
            break
        row = row + 1
    return row

def get_stacks(data):
    row = 0
    for d in data:
        if '[' not in d:
            break
        row = row + 1

    stacks = []
    row = row - 1
    c = 0
    while row >= 0:
        
        for i in range(1, len(data[row]), 4):
            if int(i/4) + 1 > len(stacks):
                stacks.append([])
            if list(data[row])[i] != ' ':
                stacks[int(i/4)].append(list(data[row])[i])
        c= c+1
        row = row -1

    return stacks


def get_nums(s):
    s = s.split(" ")
    return int(s[1]), int(s[3]), int(s[5].strip('\n'))

def operation1(stacks, a, b, c):
    while a != 0:
        item = stacks[b-1].pop()
        stacks[c-1].append(item)
        a = a - 1

def operation2(stacks, a, b ,c):
    item = stacks[b-1][-a:]
    while a!=0:
        stacks[b-1].pop()
        a=a-1

    for i in item:
        stacks[c-1].append(i)

m = movement_line(data)

###################1####################
stacks = get_stacks(data)
print(stacks)
for d in range(m, len(data)):
    a, b, c = get_nums(data[d])
    operation1(stacks, a, b, c)

print("answer1", stacks)


#############2##########################
stacks = get_stacks(data)
for d in range(m, len(data)):
    a, b, c = get_nums(data[d])
    operation2(stacks, a, b, c)

print("answer2", stacks)
