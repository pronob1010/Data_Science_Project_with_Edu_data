t = int(input())
s=0
e=0
a = ""
move2=""
for j in range(1,t+1):
    n = int(input())
    move = input()
    a = ""
    if(len(move) == (2*n -2)):
        for i in range(0, len(move)):
            if move[i]=='E':
                move2+='S'
            else:
                move2 += 'E'

        print("Case #%d: %s" % (j, move2))
        move2=""

