class Vehicle:
    def __init__(self,name,speed,mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage
class Bus(Vehicle):
    pass
School_bus = Bus("Volvo Bus", "100 mph","20")
print("The bus name is:", School_bus.name,"the speed is: ", School_bus.speed,"the mileage is:", School_bus.mileage)
