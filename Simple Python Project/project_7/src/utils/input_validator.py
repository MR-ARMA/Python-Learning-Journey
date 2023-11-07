from src.game_logic.scorer import Scorer


def get_valid_input(start, end):
    while True:
        try:
            user_input = int(input(f'Enter your guess, a number between {start} and {end}: '))
            if start <= user_input <= end:
                return user_input
            else:
                print(f'I sayed number between {start}, {end}!!')
                continue
        except ValueError:
            print("just enter 'NUMBER!!!!!'")
            return "ValueError"


