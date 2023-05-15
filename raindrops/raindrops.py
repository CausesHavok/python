"""Convert a number into a sound based on the factors of the number"""
def convert(number):
    """Convert a number into a sound based on the factors of the number

    :param number int: A given number
    :return str: A sound or number converted to str

    Determine the raindrop sound of a number based on the following rules
    if the number has a factor of 3 then "pling" is returned
    if the number has a factor of 5 then "plang" is appened
    if the number has a factor of 7 then "plong" is appened
    if the number has none of the above return the number as a string
    """
    raindrop_sound = "pling" if number % 3 == 0 else ""
    raindrop_sound += "plang" if number % 5 == 0 else ""
    raindrop_sound += "plong" if number % 7 == 0 else ""
    return raindrop_sound if raindrop_sound else str(raindrop_sound)
