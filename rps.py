import random

class RPS:
    def __init__(self):
        self.available_coice = ['rock', 'paper', 'scissors']

        self.wincon = {
            'rock' : 'scissors',
            'paper' : 'rock',
            'scissors' : 'paper'
        }
        self.win = 0
        self.tie = 0
        self.lose = 0

    def com_choice(self):
        return random.choice(self.available_coice)

    def find_winner(self, player, com):
        if player == com:
            return 'Tie'
        elif self.wincon == player:
            return 'Win'
        else:
            return 'Lose'
        
    def play(self):
        print('Welcome to RPS Game')

        while True:
            user_input = input("Type q for quit, rock paper or scissors").lower()
            if user_input == 'q':
                break
            if user_input not in self.available_coice:
                "Please Insert q rock paper or scissors"
                continue
            
            computer_choice = self.com_choice()
            print(f'computer choose {computer_choice}')

            result = self.find_winner(user_input, computer_choice)
            print(result)

            if result == 'Tie':
                self.tie += 1
            elif result == 'Win':
                self.win += 1
            else:
                self.lose += 1

        print(f"\n--- Game Over ---")
        print(f"Wins: {self.win}")
        print(f"Losses: {self.lose}")
        print(f"Ties: {self.tie}")

if __name__ == "__main__":
    game = RPS()
    game.play()



        