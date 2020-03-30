n = int(input())
arr = list(map(int, input().split()))
listnew=[]
for i in arr:
    if i not in listnew:
        listnew.append(i)

listnew.sort()
print(listnew[-2])