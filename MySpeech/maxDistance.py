ara=[3,5,4,2]
index =[]
for i in range(0, len(ara)):
    index.append(i)

for i in range(0, len(ara)):
    for j in range(i+1, len(ara)):
        if ara[i] > ara[j]:
            temp = ara[i]
            temp_index = index[i]

            ara[i] = ara[j]
            index[i] = index[j]

            ara[j] = temp
            index[j] = temp_index


max = 0
for i in range(0, len(ara)):
    for j in range(i+1, len(ara)):
        x = j-i
        if index[i] <= index[j] and max < x:
            max = x

print(max)