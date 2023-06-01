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
