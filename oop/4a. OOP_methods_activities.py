# Learning intentions:
# - Create a method (function belonging to a class)
# - Discuss the use of attributes in the method

class Pet:
    def __init__(self, name, category, age = 0,vaccinated = False, account_balance = 100):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.account_balance = account_balance
    
    def have_birthday(self):
        self.age += 1

    def vaccination(self):
        self.vaccinated = True
    
    def clear_card(self):
        self.account_balance = 0
    
    def convert_years(self):
        self.age = self.age* 6
    
    def __str__(self):
        return '|name: '+str(self.name)+'|category: '+str(self.category)+'|age: '+str(self.age)+'|Credit Card:'+str(self.ccard)+'|vaccinated:'+str(self.vaccinated)+'|Account Balance:'+str(self.account_balance)+'|'

p1 = Pet('Ringo','Cat',6, vaccinated = False, account_balance = 100)


p1.vaccination()
p1.convert_years()
p1.clear_card()
print(p1)



#ACTIVITIES:
#1. Add another method to vaccinate the pet
#2. Add another attribute for account balance then add a method to clear balance
#3. Add a method to print the animals age in human years use a multiplier of 7 if animal is a dog and a multiplier of 6 if it is a cat
# Use print statements to ensure you have comeplted each activity correctly.