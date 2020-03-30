data = input().split(" ")

a,b,c,d = data

x= int(a)+int(b)
y= int(c)+int(d)

if ((int(b)>int(c))and(int(d)>int(a)) and (int(y)>int(x))):
    if((int(c)>0)and(int(d)>0)):
        if(int(a)%2==0):
            print("Valores aceitos")
else:
    print("Valores nao aceitos")