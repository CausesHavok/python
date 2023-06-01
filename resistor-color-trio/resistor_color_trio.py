import math

"""Functions for determining the resistance of a tripple banded resistor"""
def label(colors):
    """Determine the resistor strength based on colors
    
    :param color: str - the colors of a triple banded on the resistor
    :return str - the resistance of the resistor
    """

    resistance = (color_code(colors[0])*10 + color_code(colors[1]))*10**color_code(colors[2])
    if resistance == 0:
        return "0 ohms"

    factor = math.log10(resistance)

    if factor >= 9:
        resistance = str(resistance // 10**9) + " giga"
    elif factor >= 6:
        resistance = str(resistance  // 10**6) + " mega"
    elif factor >= 3:
        resistance = str(resistance  // 10**3) + " kilo"
    else:
        resistance = str(resistance) + " "
    return resistance + "ohms"


def color_code(color: str):
    """Determine the resistor strength based on color
    
    :param color: str - the color of a band on the resistor
    :return str - the resistance of the band
    """
    return colors_code().index(color)


def colors_code():
    """Gets the list of resistor colors
    return: list[str] - the list of resistor colors
    """
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
