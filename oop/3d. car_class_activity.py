# Learning intentions:
# - Create a car class example
# - Use attributes: make, model, year and price
# - Create a __str__ method that prints make and model

class Car:
    def __init__(self,make,model,year,price=None,for_sale=False,colour='black'):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour 
        self.price = price
        self.for_sale = for_sale

    def __str__(self):
        return '|Make:  '+str(self.make)+' |Model:  '+str(self.model)+'|Year:  '+str(self.year)+'|Price:  '+str(self.price)+'|For sale: '+str(self.for_sale)+'|Colour: '+str(self.colour)+ '|' 


c1 = Car('Mazda','6',2005,'$56 987',colour='red')
c2 = Car('Sedan','3',2008,'$27 845', colour='blue')
c3 = Car('Minivan','4',2018,'$23 785',colour='green')

cars = [c1,c2,c3]

for car in cars:
    print(car)


#ACTIVITIES:
#1. Istantiate another car object
#2. Add another attribute (for_sale)
#3. Add sale status for sale or not for sale to the __str__ method
#4. Create 2 more cars and print all car statuses with a loop