"""
Author: MR-ARMA
Description: rock paper scissor game.
"""


import random


class RockPaperScissors:

    def __init__(self, ):
        self.option = ['rock', 'paper', 'scissor']

    def player_choice(self):
        player_choice = input(f'Enter your choice: {self.option}')
        player_choice = player_choice.lower()

        if player_choice in self.option:
            return player_choice
        
        else:
            print(f'I said choose one of these{self.option}!!!!')
            self.player_choice()
    
    def computer_choice(self, ):
        computer_choice = random.choice(self.option)
        return computer_choice
    
    def winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return ("Equal but not for Ever!! I'm comming soon")
        
        elif(player_choice , computer_choice) == (('rock', 'paper') or ('paper', 'scissor') or ('scissor', 'rock')):
            return("HAHA!!!!!! loser")
        
        else:
            return("You win. but just this time!")
    
    def play(self, ):
        user_choice_ = self.player_choice()
        computer_Choice_ = self.computer_choice()
        result = self.winner(user_choice_, computer_Choice_)
        print(f'your choice: {user_choice_}')
        print(f'my choice: {computer_Choice_}')
        # print(result)
        return result


if __name__ == '__main__':
    game = RockPaperScissors()

    while True:
        print(game.play())
        continue_game = input("Do you want to play again? (Enter any key to continue or 'q' to quit): ")
        if continue_game.lower() == 'q':
            break