#---begin Python ---
class Car:
    total_cars_created = 0
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.dealership = 'minchubury car city'
        Car.total_cars_created += 1
    
    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

# Instantiating objects from the Car class
car1 = Car("Toyota", "Camry", 2020, "Red")
car2 = Car("Honda", "Civic", 2018, "Blue")
car3 = Car('ford','Mustang',2021,'black')


car1.start()  # Output: Toyota Camry is starting.
car2.stop()   # Output: Honda Civic is stopping.

print(f'The amount of cars created is: {Car.total_cars_created}')
#--- end python ---
