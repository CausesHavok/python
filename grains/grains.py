"""
Functions that calculates the number of grains on a square or the board
"""

def square(number):
    """Calculate the number of grains on a square

    :param number: int - the squares number
    :return: int - number of grains on the specified square

    Function that calculates the number of grains on a square based on the squares number
    """
    if number<65 and number>0:
        return 1<<(number-1) #this is bitshifting, much faster than computing.
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    """Calculate the number of grains on the board

    :return: int - number of grains on the board

    Function that calculates the number of grains on the board
    """
    return square(64)*2-1 #this is simply math, much faster than computing
