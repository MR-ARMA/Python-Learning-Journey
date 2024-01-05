import random

def door_choice(switch_):
    choices = ['car', 'goat', 'goat']
    random.shuffle(choices)

    initial_choice = random.randint(0, 2)
    show = random.choices([i for i in range(3) if i != initial_choice and choices[i] != 'car'])

    if switch_:
        last_choice = [i for i in range(3) if i != initial_choice and i != show[0]]
    else:
        last_choice = [initial_choice]
    return choices[last_choice[0]] == 'car'


def simiulate(number=10):
    list_with_swich = list()
    for _ in range(number):
        list_with_swich.append(door_choice(switch_=True))

    list_not_swich = list()
    for _ in range(number):
        list_not_swich.append(door_choice(switch_=False))

    count_win_with_switch = list_with_swich.count(True)
    count_win_not_switch = list_not_swich.count(True)

    return count_win_with_switch, count_win_not_switch


if __name__ == "__main__":
    number_guess = 1000
    is_switch, not_switch = simiulate(number=number_guess)
    print(f"simulation with switch and {number_guess} guess: {is_switch} per sent")
    print(f"simulation without switch and {number_guess} guess: {not_switch} per sent")