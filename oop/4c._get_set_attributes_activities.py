class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0

def __str__(self):
        return '|name: '+str(self.name)+'|category: '+str(self.__category)+'|breed: '+str(self.__breed)+'|age: '+str(self.age)+'|Credit Card:'+str(self.__ccard)+'|vaccinated:'+str(self.vaccinated)+'|Weight:'+str(self.weight)+'|'
   
def set_weight(self,new_weight):
     if type(new_weight) == int or type == float:
          if new_weight > 0:
               self.weight = new_weight
          else:
                print('please enter a positive number')
     else:
            print('enter a number please!')

#ACTIVITIES:
#1. Add attribute weight and write a getter method for weight
#2. Add setter method or weight and make sure it is a positive number (integer or float)