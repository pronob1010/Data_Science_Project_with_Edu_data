n= int(input())

h= int(n/3600)
y=int(n%3600)
m=int(y/60)
s=int(y%60)

print("{}:{}:{}".format(h,m,s))