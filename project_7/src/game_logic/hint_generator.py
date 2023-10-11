def provide_hint(guess, actuall_number):
    if guess < actuall_number:
        return "your guess is too low"
    elif actuall_number < guess:
        return "your guess is too hiegh"