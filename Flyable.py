# Duck multiple inheritance

class Flyable:
    def fly(self):
        print("Flying...")
        
class Swimmable:
    def swim(self):
        print("Swimming...")
        
class Duck(Flyable, Swimmable):
    # No need to override if you're not modifying the behavior
    pass

# Creating an instance of Duck
duck1 = Duck()

# Calling inherited methods
duck1.swim()
duck1.fly()
