""" 
Functions for calculating the
sum of squares
square of sum
and difference between the above
"""
def square_of_sum(number):
    """ Calculate square of sum

    :param number int: the number
    :return int: the square of the sum
    """
    return ((number+1)*number/2)**2


def sum_of_squares(number):
    """ Calculate sum of squares

    :param number int: the number
    :return int: the sum of the square
    """
    return number*(number+1)*(2*number+1) / 6


def difference_of_squares(number):
    """ Calculate the difference between the sum of square and square of sum

    :param number int: the number
    :return int: the difference between som of squares and square of sum
    """
    return square_of_sum(number)-sum_of_squares(number)
