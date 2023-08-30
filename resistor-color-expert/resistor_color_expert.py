import math

"""Functions for determining the resistance of resistors up to and including 5 bands"""
def resistor_label(colors: list[str]):
    """Determine the resistor strength based on colors works for upto 5 bands
    
    :param color: str - the colors of the bands on the resistor 
    :return str - the resistance of the resistor and its tolerance
    """

    band_count = len(colors)
    multiplier = 0
    tolerance = ""
    if band_count > 3: # Resistors with 4 or 5 bands have a tolerance band as the last band
        tolerance = get_tolerance(colors.pop())
        band_count -= 1

    if band_count > 2: # resistors with at least 3 bands have a multiplier band located last or if there is a tolerance band, second to last
        multiplier = get_color_value(colors.pop())
        band_count -= 1

    resistance = 0
    for index, color in enumerate(colors):
        resistance += get_color_value(color) * 10 ** (band_count - index - 1)
    resistance = int(resistance*10**multiplier)

    message = resistance_to_string(resistance) + " " + tolerance
    return message.strip()


def get_color_value(color: str):
    """Determine the resistor strength based on color
    
    :param color: str - the color of a band on the resistor
    :return str - the resistance of the band
    """
    colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return colors.index(color)


def resistance_to_string(resistance: float):
    """Convert a flat resistance value to a pretty string using prefix multipliers like kilo

    :param resistance: int - the flat resistance of the resistor
    :return str - the resistance written with a prefix multiplier
    Example. Input = 3000 => output = 3 kiloohms
    """
    prefixe_multiplier = ""
    if resistance >= 1000000000:
        resistance = resistance / 1000000000
        prefixe_multiplier = "giga"
    elif resistance >= 1000000:
        resistance = resistance / 1000000
        prefixe_multiplier = "mega"
    elif resistance >= 1000:
        resistance = resistance / 1000
        prefixe_multiplier = "kilo"
    
    if resistance == int(resistance):
        resistance = int(resistance)
    return str(resistance) + " " + prefixe_multiplier + "ohms"


def get_tolerance(color: str):
    """Determine the resistor strength based on color
    
    :param color: str - the color of a band on the resistor
    :return str - the resistance of the band
    """
    colors = ["grey", "violet", "blue", "green", "brown", "red", "gold", "silver"]
    tolerances = ["±0.05%", "±0.1%", "±0.25%", "±0.5%", "±1%", "±2%", "±5%", "±10%"]
    tolerance_dict = dict(zip(colors, tolerances))

    return tolerance_dict[color]