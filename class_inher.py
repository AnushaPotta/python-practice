class Animal:
    def __init__(self, name):
        self.name = name
    

    def sound(self):
        print(f"some generic sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):   
        print(f"{self.name} meows")

dog = Dog("Buddy")

cat = Cat("Kitty")

dog.sound()
cat.sound()


        