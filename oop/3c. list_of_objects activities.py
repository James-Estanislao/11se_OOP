# Learning intentions:
# - Create a list of pets
# - Use a for loop to print out various information about pets

class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False

    def __str__(self):
        my_status = 'name: ' +  self.name   +   'category: ' +  self.category + 'age: ' + str(self.age) +' Credit Card: ' + self.ccard + ' Vaccinated: ' + str(self.vaccinated)
        return my_status

p1 = Pet(name = 'Engineer ', category =  'Dog ', vaccinated = True)
p2 = Pet(name = 'Claude',  category = 'Cat', age = 8 , vaccinated = True)
p3 = Pet(name = 'Scotty boy', category = 'Snake', age = 6 , vaccinated = True)

pets = [p1, p2, p3]

for pet in pets:
    print(pets)
    print(' ')


#ACTIVITIES:
#1. Add another pet to the list (try different methods)
#2. Vaccinate each pet in the list