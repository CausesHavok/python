import math


def label(colors):

    resistance = (color_code(colors[0])*10 + color_code(colors[1]))*10**colors_code().index(colors[2])
    if resistance == 0:
        resistance = "0 "
    elif math.log10(resistance)>=9:
        resistance = str(resistance // 10**9) + " giga"
    elif math.log10(resistance)>=6:
        resistance = str(resistance  // 10**6) + " mega"
    elif math.log10(resistance)>=3:
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
