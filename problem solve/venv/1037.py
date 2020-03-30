n = input()

if(float(n)<0 or float(n)>100):
    print("Fora de intervalo")

elif(float(n)>=0 and float(n)<=25):
    print("Intervalo [0,25]")
elif(float(n)>=25 and float(n)<=50):
    print("Intervalo (25,50]")
elif(float(n)>=50 and float(n)<=75):
    print("Intervalo (50,75]")
elif(float(n)>=75 and float(n)<=100):
    print("Intervalo (75,100]")