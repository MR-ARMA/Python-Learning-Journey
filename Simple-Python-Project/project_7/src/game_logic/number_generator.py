import random

def number_generator(start: int, end: int) ->int:
    """
    generate integer number from {start} to {end}
    """
    return random.randint(start, end)