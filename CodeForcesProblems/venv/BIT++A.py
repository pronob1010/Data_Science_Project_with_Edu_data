r=int(input())
n=0
for i in range(r):
    s = input()
    if(s=="X++" or s=="++X"):
        n += 1
    else:
        n -= 1

print(n)