a = input()
b = input()
c=0
for i in range(len(a)):
    if (a[i].lower() < b[i].lower()):
        c = -1
        break
    if (a[i].lower() > b[i].lower()):
        c = 1
        break
print(c)


