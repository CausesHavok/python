"""
Function that calcualtes the Collatz Conjecture number
"""
def steps(number):
    """ calculate the Collatz Conjecture number

    :param number int: the number
    :return int: the Collatz Conjecture number
    """
    if number<1:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while number != 1:
        number = number/2 if number % 2 == 0 else number * 3 + 1
        count += 1

    return count
