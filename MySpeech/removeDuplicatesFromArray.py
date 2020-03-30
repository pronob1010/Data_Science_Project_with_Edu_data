def array(ara):
    c = 1
    for i in range(1, len(ara)):
        if (ara[i] != ara[i - 1]):
            ara[c] = ara[i]
            c += 1
    return c
if __name__== "__main__":
    ara=[1,2,3,3,4,4,5,6]
    x = array(ara)
    print(ara[:x])

