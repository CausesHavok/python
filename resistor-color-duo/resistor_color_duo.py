"""Functions for calculating the resistance of a two color resistor"""
def value(colors):
    """Calculates the resistance of the first two bands of a resistor ignoring all but the first two colors
    :param colors: list[str] - a list of colors on a resistor
    :return int - resistance of the resistor"""
    return color_code(colors[0])*10 + color_code(colors[1])


def color_code(color: str):
    """Determine the resistor strength based on color
    
    :param color: str - the color of a band on the resistor
    :return str - the resistance of the band
    """
    return colors().index(color)


def colors():
    """Gets the list of resistor colors
    return: list[str] - the list of resistor colors
    """
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]