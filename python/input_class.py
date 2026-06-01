'''
I asked google Gemini "How to ask my end user to allocate integers to an object in a class.' 
and 'how to put it in a method' 
this is what it came up with
'''
class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def request_score_allocation(self):
        """Prompts the user via CLI to allocate a score to this player."""
        while True:
            user_input = input(f"Enter a score to allocate to {self.name}: ")
            try:
                # Convert input to integer and allocate it to the object
                self.score = int(user_input)
                print(f"Success! {self.name}'s score is now: {self.score}\n")
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")

# --- How to use it ---

# Create two different player objects
player1 = Player("Alice")
player2 = Player("Bob")

# Call the method on each object
player1.request_score_allocation()
player2.request_score_allocation()