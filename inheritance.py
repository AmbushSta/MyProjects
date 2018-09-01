class Vehicle():
    
    def __init__(self):
        self.is_a_vehicle = True # Object variable for all Vehicles
        self.print_myself = {    # Map each object to the correct method
            Car : self.car_print,
            Bike : self.bike_print   
        }

    def __str__(self):
        return self.print_myself[type(self)]()  # Reduce if statement chain by mapping
    
    def car_print(self):
        return "I am a car!"    
        
    def bike_print(self):
        return "I am a bike!"
    
class Bike(Vehicle):
    
    def __init__(self):
        super().__init__()     # Calling parent __init__ method
        self.wheel_count = 2   # Object variable for only Bike objects
        
class Car(Vehicle):
    
    def __init__(self):
        super().__init__()
        self.wheel_count = 4
        
car = Car()
print(car) # I am a car!
print("but am I a vehicle?", car.is_a_vehicle) # but am I a vehicle? True
bike = Bike()
print(bike) # I am a bike!
