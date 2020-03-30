
class Mamal:
    def sound(self):
        print("Its good")


class Dog(Mamal):
    def Only(self):
        print("great")


class Cat(Mamal):
    pass


ob = Dog()
ob.sound()
ob.Only()

