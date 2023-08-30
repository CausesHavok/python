"""Function for converting a positive integer into a roman numeral"""
def roman(number: int):
    """ Converts a positive integer to roman numeral

    :param number: int - a positive integer
    :return: str - a roman numeral
    """
    roman_numerals = {}
    roman_numerals[1] = "I"
    roman_numerals[4] = "IV"
    roman_numerals[5] = "V"
    roman_numerals[9] = "IX"
    roman_numerals[10] = "X"
    roman_numerals[40] = "XL"
    roman_numerals[50] = "L"
    roman_numerals[90] = "XC"
    roman_numerals[100] = "C"
    roman_numerals[400] = "CD"
    roman_numerals[500] = "D"
    roman_numerals[900] = "CM"
    roman_numerals[1000] = "M"

    roman_integers=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    roman_number = ""
    while(number>0):
        for roman_integer in roman_integers:
            if number >= roman_integer:
                roman_number += roman_numerals[roman_integer]
                number -= roman_integer
                break

    return roman_number
