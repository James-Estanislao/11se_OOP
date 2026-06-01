class Fighter:
    def __init__(self,name,health,weapon,armour,strength,speed,magic):
        self.name = name
        self.health = health
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
    


    def 



You = Fighter('You', 100, 30, 20, 0, 0 ,0)

You.create_character()


print(You)