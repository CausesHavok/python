"""Functionality for determining if a isbn is a valid isbn"""

def is_valid(isbn:str):
    """Determines if a isbn is a valid isbn
    
    :param isbn str: An isbn number
    :return bool: Is isbn number valid
    Determines if the isbn number is valid based on the isbn check sum
    """
    scrubbed_isbn = isbn.replace('-', '').lower()
    if len(scrubbed_isbn) != 10:
        return False

    control_sum = 0
    for index, digit in enumerate(scrubbed_isbn):
        if digit in ("0123456789"):
            control_sum += int(digit)*(10-index)
        elif digit == "x":
            control_sum += 10
        else:
            return False
    
    return control_sum % 11 == 0
