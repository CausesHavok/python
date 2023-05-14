""" Determine if year is leap year"""
def leap_year(year):
    """ Determine if year is leap year

    :param year int: A year
    :return bool: Is leap year
    Determine if the year is a leap year based on the following rules
    a) if year % 4 = 0 then it is a leap year, unless b
    b) if year % 100 = 0, unless c
    c) if year % 400 = 0.
    """

    return not(year % 4) and (year % 100 !=0 or year % 400 == 0)
