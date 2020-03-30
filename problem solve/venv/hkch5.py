n = int(input())
b = list(map(int,input().split()))
newlist=[]
for i in b:
    newlist.append(i)

print(sum(newlist))
