password = 'hello'

for a in range(3):
    psw = input("Enter ")
    b=2
    if(psw == password):
        print("Done")
        break
    else:
        print("Bal...try again",b-a)
        continue
if b-a==0:
    print("Chance Over")