T = int(input())
lst = []
while T:
    T -= 1
    s = input()
    lst.append(s)
# print(lst)
lst.sort(key=lambda x: (x[6:], x[:2], x[3:5]))
print("\n".join(lst))

