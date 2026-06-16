'''
I asked Google Gemini 
'how would i let users choose a weapon in a text based game using python'
and this what it came up with.
I'm going to use this so that players can choose their
magic spells in my game
'''
def choose_weapon():
    # 1. Define weapons with their names and stats
    weapons = {
        "1": {"name": "Sword", "damage": 10},
        "2": {"name": "Bow", "damage": 8},
        "3": {"name": "Staff", "damage": 12}
    }
    
    print("Choose your weapon:")
    # 2. Dynamically display the options using a loop
    for key, stats in weapons.items():
        print(f"{key}. {stats['name']} (Damage: {stats['damage']})")
        
    while True:
        # 3. Capture user input
        choice = input("\nEnter the number of your weapon: ").strip()
        
        # 4. Validate the input to prevent game crashes
        if choice in weapons:
            chosen_weapon = weapons[choice]
            print(f"\nYou have equipped the {chosen_weapon['name']}!")
            return chosen_weapon
        else:
            print("Invalid choice. Please pick a number from the list.")

# Start the function
player_weapon = choose_weapon()