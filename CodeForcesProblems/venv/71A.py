n = int(input())

for i in range(n):
    c = input()
    x = int(len(c))
    if (x>10):
        x-=2
        print(c[0], end="")
        print(x,end="")
        print(c[x+1])
    else:
        print(c)