"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def sublist(list_one: list[int], list_two: list[int]):
    """ Determine if a given list is a sub-, super- or equivalent of another given list

    :param list_one list[int]: List of integerers to be compared
    :param list_two list[int]: List of integerers to be compared with
    :return sublist category: The category

    Determines if list_one is a sublist, superlist or an equivalent list of list_two.
    """
    if list_one == list_two:
        return EQUAL
    
    if len(list_one) < len(list_two):
        return SUBLIST if is_sublist(list_one,list_two) else UNEQUAL
    
    if len(list_one) > len(list_two):
        return SUPERLIST if is_sublist(list_two,list_one) else UNEQUAL

    return UNEQUAL


def is_sublist(short_list: list[int], long_list: list[int]):
    """ Determine short_list is a sublist of long_list

    :param short_list list[int]: List of integerers to be compared
    :param long_list list[int]: List of integerers to be compared with
    :return boolean: Is short_list a sublist of long_list

    Determine short_list is a sublist of long_list
    """
    short_list_length = len(short_list)
    for long_counter in range(len(long_list) - short_list_length + 1):
        if long_list[long_counter:long_counter + short_list_length] == short_list:
            return True
    return False
