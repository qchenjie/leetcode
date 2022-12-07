l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

res = []
i = 0
j = 0
while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        res.append(l1[i])
        i += 1
    else:
        res.append(l2[j])
        j += 1
if i < 15:
    res.extend(l1[i:])
elif j < 15:
    res.extend(l2[j:])

for item in res:
    print(item, end=" ")