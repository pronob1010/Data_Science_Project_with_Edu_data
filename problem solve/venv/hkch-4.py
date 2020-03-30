al=0
bo=0
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(0,3):
    if(a[i]>b[i]):
        al+=1

    elif(a[i]<b[i]):
        bo+=1

print(al, end=' ')
print(bo)
