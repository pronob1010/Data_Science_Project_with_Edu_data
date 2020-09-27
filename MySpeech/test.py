
#Test before your attemp:

def ggt(a, b):
    if b == 0:
        return a
    return ggt(b, a % b)
a = 1891
b = 4819
print(ggt(a,b))
l=3
ls=[217, 1891, 4819]
for i in range(l - 1):
    if ls[i] != ls[i + 1]:
        print("bal")

orig=[-1, 31, 61,-1]
primes = sorted(list(set(orig)))
print(primes)


print("--------------------")

a= [[1,3],[2,6],[15,18],[8,10],[3,10]]
a.sort()
print(a)

print("------------------------")

alp=[]
for i in range(26):
    alp.append(chr(ord('A')+i))
print(alp)

print("------------------------")

a= [[1,3],[2,6],[15,18],[8,10],[3,10]]
a.sort()
print(a)

import bisect
b = [2,4]
bisect.insort(a,b)
print(a)

print("------------------------")
b = [[5,8],[9,11],[12,15],[15,22]]
n = [1,13]

l = len(b)
x= bisect.bisect(b,n)
if (b[x-1]> n) and (n < b[x]):
    bisect.insort(b,n)

print(b)

print("------------------------")
import math
print(math.factorial(200))
print("------------------------")

print(1/2)