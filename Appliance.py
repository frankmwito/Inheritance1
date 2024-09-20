# Appliance inheritance

class Appliance:
    def __init__(self, name, power_consumption):
        self.name = name
        self.power_consumption = power_consumption
        
    def turn_on(self):
        print(f"{self.name} is turned on")
    
    def turn_off(self):
        print(f"{self.name} is turned off")
        
class WashingMachine(Appliance):
    def __init__(self, name, power_consumption, capacity):
        super().__init__(name, power_consumption)
        self.capacity = capacity
        
    def turn_on(self):
        if self.capacity > 0:
            super().turn_on()  # Call the parent class's turn_on method
        else:
            print("Washing machine is empty, cannot be turned on.")
    
    def turn_off(self):
        if self.power_consumption > 150:
            super().turn_off()  # Call the parent class's turn_off method
        else:
            print(f"{self.name} is not consuming much power, so no need to turn off.")
    
    def wash(self):
        if self.capacity > 0:
            print(f"{self.name} is washing with a capacity of {self.capacity} kg.")
        else:
            print("Cannot start washing, the machine is empty.")


# Creating an instance of WashingMachine and using its methods
washing_machine1 = WashingMachine("LG", 100, 200)

washing_machine1.turn_on()
washing_machine1.turn_off()
washing_machine1.wash()
