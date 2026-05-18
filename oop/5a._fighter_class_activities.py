#Learning Intentions
#1. Create a loop which simulates a fight and declares a winner
#2. Test the game 
#3. Implement the game with a private __health attribute

import random

class Fighter:
    def __init__(self, name,health,weapon,shield):
        self.name = name
        self.__health = health
        self.weapon = weapon
        self.shield = shield
    
    def random_attack(self):
        attak_power = random.randint(self.weapon/2, self.weapon*2)
        return attak_power


you = Fighter('you',100,60,20)


print(you.weapon)
print(you.random_attack())