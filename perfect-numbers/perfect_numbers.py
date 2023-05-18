"""A function to determine their category as defined by thier aliquot sum"""

def classify(number:int):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")

    sum_factors = 0
    for potential_factor in range(1,number//2+1):
        sum_factors += potential_factor if number % potential_factor == 0 else 0

    if sum_factors == number:
        return "perfect"

    return "abundant" if sum_factors > number else "deficient" 
