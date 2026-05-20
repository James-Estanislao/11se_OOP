#Learning Intentions
#1. Create a defend method that helps you repel an attack
#2. Create a loop which simulates a fight and declares a winner
#3. Test the game 

import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield
  

    def self_report(self):
        print(self.name +':', 'health: ' +str(self.health), 'weapon: ' +str(self.weapon), 'shield: ' +str(self.shield))
    
    def random_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        return attack_power
    
    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage > 0:
            self.health -= damage
            print('Damage:', damage)
        else:
            print('no damage')


you = Fighter('you',100,60,20)
troll = Fighter('Troll',150,40,50)


you.self_report()
troll.self_report()

while True:
    print('you attack the troll')
    troll.defend(you.random_attack())
    troll.self_report()
    time.sleep(1)
    print(' ')
    if troll.health <= 0:
        print('You win!')
        break
    print('The troll attacked you')
    you.defend(troll.random_attack())
    you.self_report()
    time.sleep(1)
    if you.health <= 0:
        print('You Died =(')
        break
    print(' ')


   