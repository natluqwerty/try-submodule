# day3
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

def get_res(s):
    length = len(s)
    s = list(s)
    s1 = s[0: int(len(s)/2)]
    s2 = s[int(length/2): length]

    for letter in s1:
        if letter in s2:
            return convert_letter_to_num(letter)

def convert_letter_to_num(s):
    if s.isupper() == False:
        return ord(s) - 96
    else:
        return ord(s) - 38

data= []
sum = 0
with open("input3.txt", "r") as f:
    data = f.readlines()

for d in data:
    sum = sum + get_res(d)

print(f"First {sum}")


#######################2#################

def find_common_in_three(a, b, c):
    temp = [i for i in a if i in b]
    res = [i for i in temp if i in c]
    return res

sum2 = 0

for i in range(0, len(data), 3):
    l = find_common_in_three(list(data[i]), list(data[i+1]), list(data[i+2]))
    sum2 = sum2 + convert_letter_to_num(l[0])

print(f"Second {sum2}")




