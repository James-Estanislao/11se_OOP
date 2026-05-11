# Learning intentions:
# - Create a class pet with same information as in previous examples
# - Create an object instance of class pet

class pet:
    def __init__(self, name, category, age, vaccinated, Credit_Card,):
        self.name = name
        self.category = category
        self.age = age
        self.vaccinated = vaccinated
        self.Credit_Card = Credit_Card
        self.Owner_Name = 'unknown'
        self.Account_Balance = 0
p1 = pet('Bonnie', 'Cat', 3, True, '1234 5678 8901 2345',)
p2 = pet('Foxy', 'Dog', 8, False, '0987 6543 2109 8765')
p3 = pet('Edward', 'Bird', 2, False, '6543 7890 0129 3859')

print(p1.name)
print(p1.category)
print(p1.age)
print(p1.vaccinated)

print(p2.name)
print(p2.category)
print(p2.age)
print(p2.vaccinated)

print(p3.name)
print(p3.category)
print(p3.age)
print(p3.vaccinated)

#ACTIVITIES:
#1. Print out vaccination status of Bonnie
#2. Create another pet named Foxy who is a dog
#3. Add the following attributes to the pet class:
# - credit card
# - billing address
# - owner name (preset to unknown)
# - account balance (pre set to 0)