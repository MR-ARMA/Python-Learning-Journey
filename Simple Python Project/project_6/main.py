import random


def start():

    print(''' 
        Computer considers an integer number between [1, 100] and you must guess this number.
        Rules:
          Your guess must be integer number and if not, you loss 5 point
          Your guess must be between 1 and 100 and if not, you loss 2 point
          For each your guess that is not equall with number, you loss 1 point

          'q' for quit
        ''')
    
    rand_int = random.randint(1, 100)
    score = 100
    valid_q = False

    while True:
        user_num = input("Enter your guess: ")

        if user_num == 'q':
            valid_q = True
            break

        if not user_num.isdigit():
            score -= 5
            print("Your input not Valid")
            continue

        user_num = int(user_num)

        if (user_num > 100 or user_num < 1):
            print("The number is between 1 and 100!")
            score -= 2

        if user_num > rand_int:
            print("You guess is higher ")
            score -= 1
            continue
        elif user_num < rand_int:
            print("You guess is lower ")
            score -= 1
            continue
        elif user_num == rand_int:
            print("\n congratulations!!!! You guessed it right")
            print(f'your score is: {score}')
            break
    
    if not valid_q:
        if score == 100:
            print("Dirty Lucky!!!!")
        elif 50 <= score < 100:
            print("Very Good!")
        elif 0 < score < 50:
            print("Ok thats good!")
        elif score <= 0:
            print("You are nothing more than a fool")
    
    repeat = input("Do you want play again?('y' for yes) ")
    if repeat == 'y':
        start()
    else:
        print("OOOOOkkkkkkk!")

    




if __name__ == '__main__':
    start()
