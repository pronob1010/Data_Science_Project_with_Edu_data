print("task1")
price=[10,20,30]
t=0
for x in price:
    t+=x

print(f"Total : {t}")

print("task2")
print("(x, y)")
for item in range(0, 3):
    for item2 in range(0, 3):
        print(f"{item,item2}")


print("task3")
list1= [5, 2, 5, 2, 2]
for x in list1:
    print(f'x'*x)


print("task4")
list1= [5, 2, 5, 2, 2]
large=list1[0]
for x in list1:
    if large<x:
        large = x

print(large)

print("task3")
list2=[1,3,2,4,4,4]
list2.remove(4)
print(list2.index(4))

print("task4")
x="pronobmozumder"
print(x)
print(x.count('o'))


list2=[1,3,1,7,2,4,4,4]
list2.sort()
list2.reverse()
print(list2)

