
list_1 = [1, 3, 2, 0, 0, 23, 0, 0, 0, 0]
n_0 = 0
for k in list_1[::-1]:
    if k == 0:
        n_0 += 1
    else:
        break
list_1 = list_1[:-n_0]
print(list_1)