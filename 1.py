# day1

with open("input1.txt", "r") as f:
    message = f.readlines()

    list_sum = []
    total = 0

    for m in message:
        if m != '\n':
            int_m = int(m.replace("\n",""))
            total = int_m + total
        else:
            list_sum.append(total)
            total = 0

list_sum.sort(reverse=True)
print(list_sum[0] + list_sum[1] + list_sum[2])


