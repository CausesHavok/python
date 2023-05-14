"""Functions for determining triangle properties"""
def equilateral(sides):
    """ Determine if triangle is valid and equilateral 

    :param sides int[]: side lengths of triangle
    :return bool: Is triangle valid and equilateral
    A triangle is equilateral if all sides are the smae lenght
    A tiangle is valid if is_valid_triangle(sides) returns true
    """
    return len(set(sides))==1 and is_valid_triangle(sides)


def isosceles(sides):
    """ Determine if triangle is valid and isosceles

    :param sides int[]: side lengths of triangle
    :return bool: Is triangle valid and isosceles
    A triangle is isosceles if two or more sides are the same lenght (note overlap with equilateral)
    A tiangle is valid if is_valid_triangle(sides) returns true
    """
    return len(set(sides))<3 and is_valid_triangle(sides)


def scalene(sides):
    """ Determine if triangle is valid and scalene

    :param sides int[]: side lengths of triangle
    :return bool: Is triangle valid and scalene
    A triangle is scalene if no sides are the same lenght
    A tiangle is valid if is_valid_triangle(sides) returns true
    """
    return len(set(sides))==3 and is_valid_triangle(sides)

def is_valid_triangle(sides):
    """ Determine if triangle is

    :param sides int[]: side lengths of triangle
    :return bool: Is triangle valid
    A triangle is valid if
    a) for each side X the sum of the other two sides Y and Z is greater or equal ie X<=Y+Z or 2X<=X+Y+Z. It is sufficient to check for the largest side.
    b) no sides are zero
    """
    if sum(sides) >= 2*max(sides) and not 0 in sides:
        return True
    return False