number = input("Enter the value :")
data_mapping = {
    "1" : "One",
    "2" : "two",
    "3" : "Three"
}
output=""
for ch in number:
     print(data_mapping.get(ch,ch))

hey = input("Enter a sentence")
x  = input("enter your spilt char :")
print(hey.split(x))
