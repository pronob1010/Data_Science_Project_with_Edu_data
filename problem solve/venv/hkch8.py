n = int(input())
p=0
ar = []
for i in range(0,n):
    x = input()
    y = float(input())
    data= list((x,y))
    ar.append(data)

ar.sort()

min_mark = ar[0][0]
count = 0

for i in range(len(ar)):
    if min_mark == ar[i][0]:
        count = count + 1


if count >= 1:
    for j in range(count):
        ar.pop(0)


nd_min_mark = ar[0][0]
for i in range(len(ar)):
    if nd_min_mark == ar[i][0]:
        print(ar[i][1])




--------------------------------
total = []
for i in range(int(input())):
        name = input()
        score = float(input())
        name_score = list((score, name))
        total.append(name_score)
total.sort()
min_mark = total[0][0]
count = 0
for i in range(len(total)):
    if min_mark == total[i][0]:
        count = count+1
if count >= 1:
    for j in range(count):
        total.pop(0)
nd_min_mark = total[0][0]
for i in range(len(total)):
    if nd_min_mark == total[i][0]:
        print(total[i][1])
