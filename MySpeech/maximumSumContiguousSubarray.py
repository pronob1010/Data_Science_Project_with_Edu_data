ara = [-1,-2,1,2,3,-5,4,5]
try:
    n=0
    p=0
    for i in range(len(ara)):
        if(ara[i]>=0):
            p+=1
        else:
            n+=1


    if(p==len(ara)):
        print(sum(ara))

    elif(n==len(ara)):
        print(max(ara))

    else:
        maxSum=0
        currentSum=0
        for j in range(0,len(ara)):
            currentSum= ara[j]+currentSum
            if(maxSum<currentSum):
                maxSum = currentSum
            if(currentSum<0):
                    currentSum = 0
        print(maxSum)
except:
    print("array may empty")