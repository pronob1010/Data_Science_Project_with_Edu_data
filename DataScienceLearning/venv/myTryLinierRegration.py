x = {6,8,12,14,18}
y = {350,775,1150,1395,1675}

mul_sum_x=0
mul_sum_y=0

l = len(x)

mean_x= (sum(x)/l)
mean_y= (sum(y)/l)

for i in range(0,l):
    mul_sum_x +=(x[i] - mean_x)*(y[i]-mean_y)

print(mul_sum_x)