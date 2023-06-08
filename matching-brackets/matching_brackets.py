""" function for checking correctly paired () {} []"""
def is_paired(input_string: str):
    """Determines if input string has correctly paired () {} []
    
    :param input_string: str - a string
    :return: bool - are () {} [] correctly paired within string"""

    open_brackets = []
    for char in input_string:
        if char in ("(", "{", "["):
            open_brackets.append(char)
        elif char in (")", "}", "]"):
            if not open_brackets:
                return False
            if open_brackets[-1] + char in ("()", "{}", "[]"):
                open_brackets.pop()
            else:
                return False
            
    return open_brackets == []

