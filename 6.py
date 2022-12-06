with open("input6.txt", "r") as f:
    data = f.readlines()

s = data[0].strip('\n')

def get_fist_n_unique_string(s, n):
    i = 0
    j = n
    while j <= len(s) - 1:
        temp = s[i:j]
        if len(set(temp)) == n:
            print("answer", j)
            break
        i = i + 1
        j = j + 1

#######1########
get_fist_n_unique_string(s, 4)
######2########
get_fist_n_unique_string(s, 14)

