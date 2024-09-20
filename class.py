# Class multiple inheritance

# Define the Teacher class
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    
    def teach(self):
        return f"{self.name} is teaching {self.subject}."

# Define the Student class
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    
    def study(self):
        return f"{self.name} is studying {self.major}."

# Define the TeachingAssistant class that inherits from both Teacher and Student
class TeachingAssistant(Teacher, Student):
    def __init__(self, name, subject, major):
        # Initialize both parent classes
        Teacher.__init__(self, name, subject)
        Student.__init__(self, name, major)
    
    def assist(self):
        return f"{self.name} is assisting in teaching {self.subject} and also studying {self.major}."

# Create an instance of TeachingAssistant
ta = TeachingAssistant("Alice", "Mathematics", "Physics")

# Call methods from both parent classes and the TeachingAssistant class
print(ta.teach())      # Inherited from Teacher
print(ta.study())      # Inherited from Student
print(ta.assist())     # Defined in TeachingAssistant
