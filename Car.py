# Car Inheritance
from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    @abstractmethod
    def get_details(self):
        # Optional: can be abstract, or provide a base implementation
        return f"Make: {self.make}, Model: {self.model}"
    
class Sports(Car):
    def __init__(self, make, model, engine_size, num_of_doors):
        super().__init__(make, model)
        self.engine_size = engine_size
        self.num_of_doors = num_of_doors
        
    def get_details(self):
        return f"Make: {self.make}, Model: {self.model}, Engine Size: {self.engine_size}, Number of Doors: {self.num_of_doors}"
    
class Motorbike(Car):
    def __init__(self, make, model, engine_size, has_sidecar=False):
        super().__init__(make, model)
        self.engine_size = engine_size
        self.has_sidecar = has_sidecar
        
    def get_details(self):
        sidecar_status = "Yes" if self.has_sidecar else "No"
        return f"Make: {self.make}, Model: {self.model}, Engine Size: {self.engine_size}, Has Sidecar: {sidecar_status}"
    
# Creating instances and displaying details
car1 = Sports("Cadillac", "CT5V - Blackwing", "700hp", "4-door sedan")
print(car1.get_details())

motorbike1 = Motorbike("BMW", "2025", "600cc", True)
print(motorbike1.get_details())