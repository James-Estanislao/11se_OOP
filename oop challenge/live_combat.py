import time,threading
from adding_magic import distance,troll,you

def player_fighting():
    while True:
        action = input('What do you do?')
        try: #checks if player input is an integer
            action = int(action)
        except ValueError: #loop is restarted if player input isn't an integer
            print('please enter valid action.')
            continue
        if action == 1: #if player input is 1 they perform a melee attack
            troll.defend(you.melee_attack())
            print(troll)
            if troll.is_dead(): #checks if attack killed the troll
                print('you win!') #if so the game is over and you win
                break
        elif action == 2: #if player input is 2 they walk foward
            print('you walk forwards')
            you.walk_forward()
            print('distance: ', distance)
        elif action == 3: #if player input is 3 they walk backwards
            you.walk_backward()
            print('you walk back')
            print('distance: ', distance)
        elif action == 4: #if player input is 4 they rest
            print('you take a break')
            you.rest() 
            print(you)
        elif action == 5:
            print('A yellow aura eromes around you')
            you.self_heal()
        elif action == 6:
            you.hearty_sacrifice()
        elif action == 7:
            print('You cast fireball')
            troll.magic_defend(you.fireball())
            print(troll)
        print('')
 
        
    '''
    I coded an ai for the troll and gave it reactions based on the scenario
    The troll can walk forward and attack when it's in range
    The troll would walk backward when it has taken enough damage
    and the Troll decides to rest when it's too tired
    '''


def round_one():
    global distance
    while True:
        if distance == 0: #when the player is close enough the troll attacks them
            if troll.energy <= 15:
                print('the troll kneels down')
                troll.rest()
                print(troll)
            print('The troll swings at you')
            you.defend(troll.melee_attack())
            print(you)
            if you.is_dead(): #checks if trolls attack kills the player
                print('you died =( ') #if so the game ends the player loses
                break
        elif troll.energy <= 25: #if the troll is too tired they rest
            print('the troll kneels down')
            troll.rest()
            print(troll)
        elif troll.health <  40: #when the troll is low on health they walk back and retreat
            troll.walk_backward()
            print('the troll stumbles back')
            print('distance: ', distance)
        elif distance > 0: #if player is too far the troll walks forward
            troll.walk_forward()
            print('the troll approaches you')
            print('distance: ', distance)
        print('')
        time.sleep(5)

thread1 = threading.Thread(target=player_fighting)
thread2 = threading.Thread(target=round_one)

thread1.start()
thread2.start()