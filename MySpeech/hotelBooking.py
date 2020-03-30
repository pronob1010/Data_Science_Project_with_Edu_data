checkIn = [1,3,5]
checkOut = [2, 6, 8]
room = 1
r = 0
x = len(checkIn)
for j in range(0,x):
    for i in range(0,x):
        if (checkOut[j] >= checkIn[i+1]):
            r+=1
    if(room >= r):
        r=0
    else:
        print("impossible")

