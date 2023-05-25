"""Rebaseing functionality"""
import math
def rebase(input_base:int, digits:list[int], output_base:int):
    """Rebase number from basex to basey
    
    :param input_base int: base of digits
    :param digits list[int]: digits in input base
    :param output_base int: base of the output
    :return list[int]: digits in outputbase
    Rebases the input digits from input base to output base
    """
    #Input validation
    if input_base < 2: raise ValueError("input base must be >= 2")
    if output_base < 2: raise ValueError("output base must be >= 2")
    if set(digits) == {0} or digits == []: return [0]
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    
    # I am not smart enough to figure out how to convert directly from base to base, so I use base 10 as a stepping stone.
    sum_base10 = basex_to_base10(input_base, digits)
    return base10_to_basex(sum_base10, output_base)


def basex_to_base10(basex:int, digits:list[int]):
    """Rebase digits from basex to base10
    
    :param basex int: base of digits
    :param digits list[int]: digits in basex
    :return int: sum of digits in base10
    Rebases the input digits from basex to base10
    """
    sum_base10 = 0
    Number_digits = len(digits)
    for index, digit in enumerate(digits):
        sum_base10 += digit*basex**(Number_digits-index-1)
    return sum_base10



def base10_to_basex(number:int, basex:int):
    """Rebase digits from base10 to base
    
    :param number int: number in base10
    :param basex int: output base
    :return list[int]: digits in base
    Rebases the number from base10 to basex
    """
    output_digits = list()
    start_index = math.floor(math.log(number, basex))+1
    for index in reversed(range(start_index)):
        factor = basex**index
        new_digit = math.floor(number / factor)
        output_digits.append(new_digit)
        number -= new_digit*factor
    return output_digits