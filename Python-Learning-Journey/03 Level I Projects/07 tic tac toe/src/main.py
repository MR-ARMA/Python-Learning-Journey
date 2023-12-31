import random


class TicTacToe:
    def __init__(self):
        self.board = [' '] *10
        self.player_turn = self.get_random_first_palyer()

    def get_random_first_palyer(self, ):
        return random.choice(['X', 'O'])
        
    def show_board(self):
        print('\n')
        print(self.board[1], '|', self.board[2], '|', self.board[3])
        print('---------')
        print(self.board[4], '|', self.board[5], '|', self.board[6])
        print('---------')
        print(self.board[7], '|', self.board[8], '|', self.board[9])
    
    def swap_player_turn(self):
        self.player_turn = 'X' if self.player_turn == 'O' else 'O'
        return self.player_turn
    
    def is_board_fill(self):
        return ' ' not in self.board[1: ]
    
    def fix_spot(self, cell, player):
        self.board[cell] = player
    
    def has_player_won(self, player):
        win_combination = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
            [1, 5, 9], [3, 5, 7] # diagonals
        ]

        for combination in win_combination:
            if all([self.board[cell] == player for cell in combination]):
                return True
        
        return False
    
    def start(self):
        while True:
            self.show_board()
            try:
                cell = int(input(f"Player {self.player_turn} you turn, Enter the cell number: "))

                # Check if cell is in the allowed range and is empty
                if cell in range(1, 10) and self.board[cell] == ' ':
                    self.fix_spot(cell, self.player_turn)

                    if self.has_player_won(self.player_turn):
                        print(f"Player {self.player_turn} wins!")
                        print(f'player {self.swap_player_turn()} you are always are a loser!!!')
                        break

                    if self.is_board_fill():
                        print("Gameover and nobody win but why you do that?!")
                        break

                    self.swap_player_turn()

                else:
                    print("Invalid input, please try again.(Enter valit input like a gentleman)")
            except ValueError:
                print("\nInvalid input, please enter a number between 1 and 9.")
                print("we'll treat you with respect, please do the same in return. if your behaviour is unacceptable we may refuse to serve you)")


if __name__ == "__main__":
    game = TicTacToe()
    game.start()