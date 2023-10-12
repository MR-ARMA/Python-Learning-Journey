from src.utils.input_validator import get_valid_input
from src.game_logic.number_generator import number_generator
from src.game_logic.hint_generator import provide_hint
from src.game_logic.scorer import Scorer


def main():
    actuall_number = number_generator(1, 100)
    score = Scorer()

    while True:
        user_input = get_valid_input(1, 100)


        if user_input == "ValueError":
            score.decrement_score_valid()
            continue


        if user_input == actuall_number:
            print("Congratulations!!!!")
            print(f'Your score is; {score.get_score()}')
            break
        else:
            hint = provide_hint(user_input, actuall_number)
            print(hint)
            score.decrement_score_false()






if __name__ == '__main__':
    main()