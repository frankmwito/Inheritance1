# Animal class inheritance


# Base class Animal
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return ""

# Dog subclass
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        
    def make_sound(self):
        return "woof!"

# Cat subclass
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        
    def make_sound(self):
        return "meow"

# Creating instances of Dog and Cat
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Siamese")

# Calling make_sound() for both instances
print(f"{dog.name} the {dog.breed} says {dog.make_sound()}")
print(f"{cat.name} the {cat.breed} says {cat.make_sound()}")
