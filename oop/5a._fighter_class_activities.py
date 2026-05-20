#Learning Intentions
#1. Create a loop which simulates a fight and declares a winner
#2. Test the game 
#3. Implement the game with a private __health attribute

import random

class Fighter:
    def __init__(self, name,health,weapon,shield):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.shield = shield

    def self_report(self):
        print(self.name +':', 'health: ' +str(self.health), 'weapon: ' +str(self.weapon), 'shield: ' +str(self.shield))
    
    def random_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        return attack_power


you = Fighter('you',100,60,20)
troll = Fighter('Troll',150,30,50)


you.self_report()
troll.self_report()
print('you attack the troll')
troll.health -= you.random_attack()
troll.self_report()

if you.health > troll.health:
    print('You win!')
else:
    print('The troll killed you =(')