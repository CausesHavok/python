import math

"""
Function that determines if a number is an armstrong number
"""
def is_armstrong_number(number):
    """Determine if a number is an armstrong number

    :param number: int - number to be evaluated
    :return: bool - whether the number is an armstrong or not

    Function that takes a number and determines if it is an armstrong number
    """

    exponent = int(math.log10(number))+1 if number>0 else 1 #log10 is much faster/lighter than (len(str(number))), but special care has to be taken for 0
    sum_of_digits_exponented=0
    for x in str(number):
        sum_of_digits_exponented += int(x)**exponent
    return sum_of_digits_exponented == number
