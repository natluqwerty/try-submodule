# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.
# 1 for Rock, 2 for Paper, and 3 for Scissors
# def score_match(m, n):
#     if (m == 'A' and n == 'X') or (m == 'B' and n == 'Y') or (m == 'C' and n == 'Z'):
#         return 3
#     if (m == 'A' and n == 'Y') or (m == 'B' and n == 'Z') or (m == 'C' and n == 'X'):
#         return 6
#     if (m == 'A' and n == 'Z') or (m == 'B' and n == 'X') or (m == 'C' and n == 'Y'):
#         return 0

# def score_choose(j):
#     if j == 'X':
#         return 1
#     if j == 'Y':
#         return 2
#     if j == 'Z':
#         return 3

# data= []
# with open("input2.txt", "r") as f:
#     data = f.readlines()

# sum = 0
# for d in data:

#     d_list = d.split()

#     score = score_match(d_list[0], d_list[1]) + score_choose(d_list[1])
#     sum = sum + score

# print(sum)


# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.
# 1 for Rock, 2 for Paper, and 3 for Scissors
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
def score_for_match(y):
    if y == 'X':
        return 0
    if y == 'Y':
        return 3
    if y == 'Z':
        return 6


def score_for_choice(x, a):
    if a == 0: # lose
        if x == 'A':
            return 3
        if x == 'B':
            return 1
        if x == 'C':
            return 2

    if a == 3:  # tie
        if x == 'A':
            return 1
        if x == 'B':
            return 2
        if x == 'C':
            return 3

    if a == 6: # win
        if x == 'A':
            return 2
        if x == 'B':
            return 3
        if x == 'C':
            return 1

data= []
with open("input2.txt", "r") as f:
    data = f.readlines()

sum = 0

for d in data:

    d_list = d.split()

    score2 = score_for_choice(d_list[0] ,score_for_match(d_list[1]))

    score = score_for_match(d_list[1]) + score2

    sum = sum + score

print(sum)

