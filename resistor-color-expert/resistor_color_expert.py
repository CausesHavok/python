import math

"""Functions for determining the resistance of a tripple banded resistor"""
def resistor_label(colors: list[str]):
    """Determine the resistor strength based on colors
    
    :param color: str - the colors of a triple banded on the resistor
    :return str - the resistance of the resistor
    """

    "One band   - r=band1"
    "Two band   - r=band1*10 + band2"
    "three band - r=(band1*10+band2)*band3"
    "four band  - r=(band1*10+band2)*band3 +- band4"
    "five band  - r=(band1*100+band2*10+band3)*band4 +- band5"

    print(colors)
    band_count = len(colors)
    multiplier = 0
    tolerance = ""
    if band_count > 3:
        tolerance = get_tolerance(colors.pop())
        print(tolerance)
        band_count -= 1

    if band_count > 2:
        multiplier = get_color_index(colors.pop()) - 1
        print(multiplier)
        band_count -= -1

    resistance = 0
    for index, color in enumerate(colors):
        resistance += get_color_index(color) * 10 ** (band_count - index - 2)
    
    resistance = int(resistance*10**multiplier)

    if resistance == 0:
        return "0 ohms"
    print(resistance)
    factor = math.log10(resistance)

    if factor >= 9:
        resistance = str(resistance // 10**9) + " giga"
    elif factor >= 6:
        resistance = str(resistance  // 10**6) + " mega"
    elif factor >= 3:
        resistance = str(resistance  // 10**3) + " kilo"
    else:
        resistance = str(resistance) + " "
    resistance += "ohms"
    if tolerance != "":
       resistance += " " + tolerance
    print(resistance)
    return resistance


def get_color_index(color: str):
    """Determine the resistor strength based on color
    
    :param color: str - the color of a band on the resistor
    :return str - the resistance of the band
    """
    return colors().index(color)


def get_tolerance(color: str):
    """Determine the resistor strength based on color
    
    :param color: str - the color of a band on the resistor
    :return str - the resistance of the band
    """
    tolerance_colors = 


    tolerances = ["±0.05%",
                  "±0.1%",
                  "±0.25%",
                  "±0.5%",
                  "±1%",
                  "±2%",
                  "±5%",
                  "±10%"]

    return tolerances[get_color_index(color)]


def colors():
    """Gets the list of resistor colors
    return: list[str] - the list of resistor colors
    """
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]



resistor_label(["orange", "orange", "black", "red"])
resistor_label(["orange", "orange"])
resistor_label(["orange", "orange", "orange", "black", "orange"])