import random, time

attack = False
distance = 10  

class Fighter: #the fighter class being set up
    def __init__(self,name,health,energy,weapon,armour,strength,speed,magic):
        self.name = name
        self.health = health
        self.energy = energy
        self.weapon = weapon
        self.armour = armour
        self.strength = strength
        self.speed = speed
        self.magic = magic
        self.stat_points = 10  #this what is used for stat points
        self.max_health = health
        self.max_energy = energy


    def __str__(self): #this function turns objects in a class into a string so that when i print it out it looks neat
        my_status = '|name: '+str(self.name)+'|health: '+str(self.health)+'|Energy: '+str(self.energy)+'| weapon: '+str(self.weapon)+'|armour: '+str(self.armour)+'|strength: '+str(self.strength)+'|speed: '+str(self.speed)+'|magic: '+str(self.magic)+'|'
        return my_status 

    def set_strength(self): #the function used to let players allocate stat points to strength
        while True: 
            new_strength = input('Allocate points to strength ') #whatever the user inputs
            try:
                new_strength = int(new_strength) #this turns the string input into an integer
                if new_strength < 0: #checks if number inputed is negative
                    print('Number cannot be negative') 
                    continue #restarts the function
                elif new_strength > self.stat_points: #cheks if player has eniugh stat points
                    print("You don't have enough stat points")
                    continue
                self.strength += new_strength #converts the players characters strength into the player input
                self.stat_points = self.stat_points - self.strength
                print(f'Your stat points are now at {self.stat_points} and your strength is now at {self.strength}')
                break
            except ValueError: #checks if number inputted is a number
                print('please enter a number.')


    def set_speed(self): 
        while True:
            new_speed = input('Allocate points to speed ')
            try:
                new_speed = int(new_speed)
                if new_speed < 0:
                    print('Number cannot be negative')
                    continue
                elif new_speed > self.stat_points:
                    print("You don't have enough stat points")
                    continue
                self.speed += int(new_speed)
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
                elif new_magic > self.stat_points:
                    print("You don't have enough stat points")
                    continue
                self.magic += int(new_magic)
                self.stat_points = self.stat_points - self.magic
                print(f'Your stat points are now at {self.stat_points} and your speed is now at {self.magic}')
                break
            except ValueError:
                print('please enter a number.')        


    def create_character(self): #this function calls back set strength speed and magic functions 
        while self.stat_points > 0:
            self.set_strength()
            self.set_speed()
            self.set_magic()
    


    def melee_attack(self): #method that calculates an attack
        if self.energy < 15:
            print('your too tired')
        elif distance == 0: #checks if target is in range
            attack_power = random.randint(self.weapon//2, self.weapon*2) #the damage output is randomised between half of the weapons damage and double of the weapons damage
            attack_power += (self.strength*2) #melee damage is scaled up with strength
            self.energy -= 15 #melee's take away 15 energy points
            print('Attack power:', attack_power) #shows player the attack power
            return attack_power
        else:
            print('your too far') 
            


    def defend(self,attack_power): #method that simulates how damage is recieved
        if distance > 0: #to check if target is in range
            print('') #nothing happens if target is out of range
        elif self.armour > 0: #checks if target has armour
            self.armour -= round(attack_power*0.5) #If target has armour then armour takes 50%
            self.health -= round(attack_power*0.3) #target then takes 30% damage to health and 20% damage is completely mitgated
            print(self.name, 'took', round(attack_power*0.3), 'damage')
        else:
            self.health -= attack_power #if target is in range and had no armour the target takes all the damage to the health
            print(self.name, 'took', attack_power, 'damage')


    def walk_forward(self):
        global distance #must use distance as global value
        if self.energy < 25: #checks if player has enough energy to walk
            print('energy is too low') 
        elif distance == 0: #checks if the enemy is already infront of the player
            print('Your already in front of them')
        else:
            distance -= self.speed 
            self.energy -= 25
            if distance < 0:
                distance = 0
            
        
    def walk_backward(self):
        global distance #again must use distance as global value
        if self.energy < 25: #checks if player has enough energy
            print('energy is too low')
        else:
            distance += self.speed #distance is increased
            self.energy -= 25
            
    def rest(self):
        self.energy += 45
        self.health += 15 #characters energy and health are restored when they rest
        if self.health > self.max_health: #checks if players health is over max health
            self.health = self.max_health #if so this function doesn't allow health to go over max threshhold
        if self.energy > self.max_energy: #the same thing can be said for energy in this function
            self.energy = self.max_energy

    def is_dead(self):
        if self.health <= 0: #checks if character is dead
            return True 
        else:
            return False
        
     
you = Fighter('You', 100,100, 30, 100, 0, 0 ,0)
troll = Fighter('Troll',150,100, 40, 50, 6, 3, 1)


print('when creating your character consider that:')
print('strength increases your damage')
print('speed affects how far you walk')
print('and magic allows you to use unique abilities that help you in different ways.')
print('')
you.create_character()



print(you)
print(troll)


print('controls:')
print('1:melee attack')
print('2:walk forwards')
print('3:Walk forwards')
print('4:walk backwards')



while True:
    action = input('What do you do?')
    try:
        action = int(action)
    except ValueError:
        print('please enter valid action.')
        continue
    if action == 1:
        troll.defend(you.melee_attack())
        print(troll)
        if troll.is_dead():
            print('you win!')
            break
    elif action == 2:
         print('you walk forwards')
         you.walk_forward()
         print('distance: ', distance)
    elif action == 3:
        you.walk_backward()
        print('you walk back')
        print('distance: ', distance)
    elif action == 4:
        print('you take a break')
        you.rest() 
        print(you)
    print('')
    time.sleep(2)
    if distance == 0:
        if troll.energy <= 15:
            print('the troll kneels down')
            troll.rest()
            print(troll)
        print('The troll swings at you')
        you.defend(troll.melee_attack())
        print(you)
        if you.is_dead():
            print('you died =( ')
            break
    elif troll.energy <= 25:
        print('the troll kneels down')
        troll.rest()
        print(troll)
    elif troll.health <  40:
        troll.walk_backward()
        print('the troll stumbles back')
        print('distance: ', distance)
    elif distance > 0:
        troll.walk_forward()
        print('the troll approaches you')
        print('distance: ', distance)
    print('')