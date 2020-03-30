import math
linha1 = input().split(" ")
linha2 = input().split(" ")
x1,y1 = linha1
x2,y2 = linha2
Dis = math.sqrt(pow((float(x2)-float(x1)),2)+pow((float(y2)-float(y1)),2))
float(Dis)
print("%.4f"%Dis)
