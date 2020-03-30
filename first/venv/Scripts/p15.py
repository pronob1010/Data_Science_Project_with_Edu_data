class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print(f"i' work {self.name}")

person1 = Person("Pronob")
print(person1.name)
person1.talk ()

bob = Person("Joy")
print(bob.name)