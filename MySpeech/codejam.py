t = int(input())
a = ""
for j in range(1,t+1):
    num = input()

    for i in range(0,len(num)):
        if num[i] == '4':
            a+='1'
        else:
            a+='0'
    x=int(a)
    y= int(num)-int(a)
    print ("Case #%d: %d %d"%(j,x,y))
    a=''
