class Vehicle():
    
    def __init__(self):
        self.is_a_vehicle = True
        self.print_myself = {
            Car : car_print,
            Bike : bike_print   
        }

    def __str__(self):
        return self.print_myself[type(self)]()
        
class Bike(Vehicle):
    
    def __init__(self):
        super().__init__()
        self.wheel_count = 2
        
class Car(Vehicle):
    
    def __init__(self):
        super().__init__()
        self.wheel_count = 4
        
def car_print():
    return "I am a car!"
    
def bike_print():
    return "I am a bike!"
        
car = Car()
print(car) # I am a car!
print("but am I a vehicle?", car.is_a_vehicle) # but am I a vehicle? True
bike = Bike()
print(bike) # I am a bike!
