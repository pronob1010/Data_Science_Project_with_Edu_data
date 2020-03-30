x = int(input())
p=[]
y=[]
z=[]
for i in range(x):
    n = list(map(int,input().split()))
    y = n
    p = sum(y)
    z.append(p)
c=0
z = sorted(z)

for j in range(len(z)):
    if z[j]>1:
        c+=1

print(c)