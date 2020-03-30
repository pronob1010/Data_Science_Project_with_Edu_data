x,y = input().split()
c=0
p=[]
n = list(map(int,input().split()))
p=n

for j in range(len(p)):
    if ((int(p[j]) >= int(p[int(y)-1])) and (int(p[j])>0)):
        c+=1

print(c)


