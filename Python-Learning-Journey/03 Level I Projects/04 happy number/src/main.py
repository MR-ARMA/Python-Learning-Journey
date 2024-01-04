
def check_happy_number(n: int) ->bool:
    """_summary_

    Args:
        n : Enter number for check

    Returns:
        _type_: Return boolean checkers for that is happy number or is not
    """
    is_seen = set()
    while n != 1 and (n not in is_seen):
        is_seen.add(n)
        n = sum([int(i) **2 for i in str(n)])
    
    return n == 1

if __name__ == '__main__':
    assert check_happy_number(45) is True
    assert check_happy_number(44) is False