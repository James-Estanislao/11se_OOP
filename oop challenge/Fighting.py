import random, time

distance = 10

class Fighter:
    def __init__(self,name,health,energy,weapon,armour,strength,speed,magic):
        self.name = name
        self.health = health
        self.energy = energy
        self.weapon = weapon
        self.armour = armour
        self.strength = strength
        self.speed = speed
        self.magic = magic
        self.stat_points = 10


    def __str__(self):
        my_status = '|name: '+str(self.name)+'|health: '+str(self.health)+'|weapon: '+str(self.weapon)+'|armour: '+str(self.armour)+'|strength: '+str(self.strength)+'|speed: '+str(self.speed)+'|magic: '+str(self.magic)+'|'
        return my_status

    def set_strength(self): 
        while True:
            new_strength = input('Allocate points to strength ')
            try:
                new_strength = int(new_strength)
                if new_strength < 0:
                    print('Number cannot be negative')
                    continue
                self.strength = new_strength
                self.stat_points = self.stat_points - self.strength
                print(f'Your stat points are now at {self.stat_points} and your strength is now at {self.strength}')
                break
            except ValueError:
                print('please enter a number.')


    def set_speed(self):
        while True:
            new_speed = input('Allocate points to speed ')
            try:
                new_speed = int(new_speed)
                if new_speed < 0:
                    print('Number cannot be negative')
                    continue
                self.speed = int(new_speed)
                self.stat_points = self.stat_points - self.speed
                print(f'Your stat points are now at {self.stat_points} and your speed is now at {self.speed}')
                break
            except ValueError:
                print('please enter a number.')

    def set_magic(self):
        while True:
            new_magic = input('Allocate points to speed ')
            try:
                new_magic = int(new_magic)
                if new_magic < 0:
                    print('Number cannot be negative')
                    continue
                self.magic = int(new_magic)
                self.stat_points = self.stat_points - self.magic
                print(f'Your stat points are now at {self.stat_points} and your speed is now at {self.magic}')
                break
            except ValueError:
                print('please enter a number.')        


    def create_character(self):
        while self.stat_points > 0:
            self.set_strength()
            self.set_speed()
            self.set_magic()
    


    def melee_attack(self):
        if distance == 0:
            attack_power = random.randint(self.weapon//2, self.weapon*2)
            attack_power += (self.strength*3)
            self.energy -= 15
            print('Attack power:', attack_power)
            return attack_power
        else:
            print('your too far')


    def defend(self,attack_power):
        damage = attack_power - self.armour
        if damage > 0:
            print(self.name, 'took', damage, 'damage')
            self.health -= damage
        else:
            print(self.name, 'defended the attack')

    def walk_forward(self):
        global distance
        if self.energy < 25:
            print('energy is too low')
        elif distance == 0:
            print('Your already in front of them')
        else:
            distance -= self.speed
            self.energy -= 30
            if distance < 0:
                distance = 0
            print('distance:', distance)
        
    def walk_backward(self):
        global distance
        if self.energy < 25:
            print('energy is too low')
        else:
            distance += self.speed
            self.energy -= 30

    def rest(self):
        self.energy += 45
        self.health += 15

    def is_dead(self):
        if self.health == 0:
            return True
        else:
            return False
        

     
you = Fighter('You', 100,100, 30, 20, 0, 0 ,0)
troll = Fighter('Troll',150,100, 30, 0, 6, 3, 1)


print('when creating your character consider that: strength increases your damage, speed affects how far you walk' \
'and magic allows you to use unique abilities that help you in different ways.')

you.create_character()



print(you)
print(troll)


print('controls:1 is for melee attack, 2 is to walk forward, 3 is to walk back, 4 is to rest')

while True:
    action = input('What do you do?')
    action = int(action)
    if action == 1:
        troll.defend(you.melee_attack())
        print(troll)
        if troll.is_dead:
            print('you win!')
            break
    elif action == 2:
         print('you walk forwards')
         you.walk_forward()
    elif action == 3:
        you.walk_backward()
        print('you walk back')
    elif action == 4:
        print('you take a break')
        you.rest() 
        print(you)
    else: 
        print('please enter valid action.')
        continue
    time.sleep(2)
    if troll.energy <= 25:
        print('the troll kneels down')
        troll.rest()
        print(troll)
    elif distance == 0:
        you.defend(troll.melee_attack())
        print(you)
        if you.is_dead:
            print('you died =( ')
            break
    elif troll.health <  40:
        troll.walk_backward()
        print('the troll stumbles back')
    elif distance > 0:
        troll.walk_forward()
        print('the troll approaches you')