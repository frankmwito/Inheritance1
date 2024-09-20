# person inheritance
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @abstractmethod
    def walk(self):
        return f"walk normally {self.name} of {self.age} years"
    
    
class Athlete(Person):
    def walk(self):
        return f"walk faster {self.name} of {self.age} years"
    
    
person1 = Athlete("frank", 22)

print(person1.walk())