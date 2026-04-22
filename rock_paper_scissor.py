import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.win_rules = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        self.wins = 0
        self.losses = 0
        self.ties = 0
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def determine_winner(self, player, computer):
        if player == computer:
            return "Tie"
        elif self.win_rules[player] == computer:
            return "You Won"
        else:
            return "You Lost"
    
    def play(self):
        print('Welcome to Rock Paper Scissors!')
        
        while True:
            user_input = input("\nEnter choice (rock, paper, scissors) or 'q' to quit: ").lower()
            
            if user_input == "q":
                break
            
            if user_input not in self.choices:
                print('Please enter one of: rock, paper, scissors')
                continue
            
            comp_choice = self.get_computer_choice()
            print(f"Computer chose: {comp_choice}")
            
            result = self.determine_winner(user_input, comp_choice)
            print(result)
            
            # Track stats
            if result == "You Won":
                self.wins += 1
            elif result == "You Lost":
                self.losses += 1
            else:
                self.ties += 1
        
        # Show final stats
        print(f"\n--- Game Over ---")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Ties: {self.ties}")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()