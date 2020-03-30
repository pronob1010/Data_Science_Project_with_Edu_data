linha1 = input().split(" ")
A,B,C = linha1

pi= 3.14159
T= (.5* float(A) * float(C))
Rc= float(pi)*float(C)*float(C)
Tr= ((float(A)+float(B))/2)*float(C)
S= (float(B)*float(B))
R= float(A)*float(B)
print("TRIANGULO: %.3f"%T)
print("CIRCULO: %.3f"%Rc)
print("TRAPEZIO: %.3f"%Tr)
print("QUADRADO: %.3f"%S)
print("RETANGULO: %.3f"%R)