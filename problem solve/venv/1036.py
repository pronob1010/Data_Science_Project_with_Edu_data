import math
data= input().split(" ")
A,B,C = data
x=(float(B)*float(B)-4*float(A)*float(C))
y = math.sqrt(x)
R1=(float(B*(-1))+y)/(2*float(A))
R2=(float(B*(-1))-y)/(2*float(A))
if((A==0)or(x<0)):
    print("Impossivel calcular")
else:
    print("R1 = %.5f"%R1)
    print("R2 = %.5f"%R2)