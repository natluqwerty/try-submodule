def if_fully_contains(a, b, c, d):
    if (a >= c and b <= d) or (a <= c and b >= d):
        return 1
    return 0

def get_nums(s):
    s = s.split('-')
    temp = s[1].split(',')
    # DO NOT FORGET TO CONVERT STRING TO INT!!!!!!!! 😠😿
    return int(s[0]), int(temp[0]), int(temp[1]), int(s[2])

data= []
with open("input4.txt", "r") as f:
    data = f.readlines()

sum = 0
for d in data:
    a, b, c, d = get_nums(d)
    sum = if_fully_contains(a, b, c, d) + sum

print("answer1",sum)

##########2##########
def overlap(a, b, c, d):
    if b < c or d < a:
        print(a,b,c,d)
        return 0
    return 1

sum2 = 0
for d in data:
    a, b, c, d = get_nums(d)
    sum2 = overlap(a, b, c, d) + sum2

print("answer2",sum2)