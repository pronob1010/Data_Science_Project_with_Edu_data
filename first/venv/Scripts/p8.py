number = input("Enter the Number")
digit_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output = ""
for ch in number:
    print(digit_mapping.get(ch, "!"))


print("Task-2")
text = input(">")
word = text.split(' ')
print(word)



print("Task-3")
text = input(">")
word = text.split(' ')
print(word)



