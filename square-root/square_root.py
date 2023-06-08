""" Two functions for finding the suare root of a number without using libraries"""
def square_root(number: int):
    """Finds the square root of a number 
    
    :param number: int - a given number with a root that is a natural number
    :return :int - the square root of the input
    This method finds the square root of a number by testing every number x from 1 to the number
    It terminates when x*x = number
    """
    natural_number = 0
    while natural_number*natural_number != number:
        natural_number += 1
    return natural_number

def square_root2(number: int):
    """Finds the square root of a number 
    
    :param number: int - a given number with a root that is a natural number
    :return :int - the square root of the input
    This method finds the square root of a number by performing a binary search on the number.
    It tries to take advantage of the fact that the square root of a number is much closer to 1 than to the number
    So we start by simple finding an upper bound by doubling and then binary searching within that space.
    I tried doing other fancy stuff like using log10 or log2 to get some initial bounds, but the time it takes to
    load the package is much greater than the time it takes to actually perform the calculations. Even for very large numbers
    """
    n = 1
    upper_cap = 1
    lower_cap = 1

    while n*n < number:
        n *= 2
    
    while n*n != number:
        if n*n > number:
            upper_cap = n
        else:
            lower_cap = n
        n = (upper_cap + lower_cap) // 2
    return n
