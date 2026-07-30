days = 0

def start_day():
    global days
    while True:
        try:
            action = int(input('as the morning day breaks what do you do?'))
        except ValueError:
            print("you can't do that..")
        print('input 1 to check fridge, input 2 to board window,')
        if action == 1:
            print("there's nothing in the fridge")
        if action == 2:
            print('you board the window')
        if action == 3:
            print(days)
            break
        days += 1

start_day()