deng = 7
l = input()
st = -1
st = int(st)
rS=0
rS = int(rS)
o = "NO"


for i in range(len(l)):
    if(l[i] != st):
        st = l[i]
        rS=0
    rS+=1
    if(rS >= deng):
        o = "YES"
        break

print(o)
