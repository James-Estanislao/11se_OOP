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

    def set_speed(self, new_speed):
        new_speed = input('Allocate points to speed')
        if type(new_speed) == int or type(new_speed) == float:
            if new_speed > 0:
                self.speed = new_speed
            else:
                print('Please enter a positive number for speed')
                set_speed()
        else:
            print('Please enter a number for speed')
            set_speed()

    def set_magic(self, new_magic):
        new_magic = input('Allocate points to magic')
        if type(new_magic) == int or type(new_magic) == float:
            if new_magic > 0:
                self.magic = new_magic
            else:
                print('Please enter a positive number for magic')
                set_magic()
        else:
            print('Please enter a number for magic')
            set_magic()


while self.stat_points > 0:
    new_strength = input('Allocate points to strength ')
    self.strength = new_strength
    self.stat_points = self.stat_points - new_strength

You = Fighter('You', 100, 30, 20, 0, 0 ,0)

You.set_speed(new_speed=0)

print(You)