# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return "Some Sound"

# class Dog(Animal):
#     def __init__(self, name,  breed):
#         super().__init__(name )
#         self.breed = breed
#     def speak(self):
#         return "Woof"



# a = Animal("Dog")
# d = Dog("Dog","Spaniel")

# print(a.speak())
# print(d.speak())



# Create a base class Vehicle:
# 	•	__init__(brand)
# 	•	describe() returns "This is a vehicle by <brand>"

# Create a subclass Car(Vehicle):
# 	•	__init__(brand, model) → use super() for brand
# 	•	describe() should return "This is a car: <brand> <model>"


class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def describe(self):
        return f"This is a vehicle used by {self.brand} "

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__( brand)
        self.model = model
    
    def describe(self):
        return f"This is a car {self.brand} {self.model}"


v1 = Vehicle("Tata")
c1 = Car("Tata","Nixon")

print(v1.describe())
print(c1.describe())

