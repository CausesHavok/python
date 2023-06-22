""" functions for determining the answer to a mathematical question formulated in plain english"""
def answer(question:str):
    """ Evaluate the result of a mathematical question formulated in plain english
    :param question: str - a question
    :return: float - the answer to the question
    The method works by 
    !) Replacing plain english with operators
    2) Trimming to contain what should be only values and operators, otherwise it is an unknown operations error
    3) Looping through all the parts of the question and
    3.1) The first and every other part should be a number, otherwise it is a syntax error
    3.2) The sedond and every other part should be an operator, otherwise it is a syntax error
    3.3) Performning the operations on the values
    4) Finally we check to make sure we ended on a value, otherwise it is a syntax error
    """
    #Replace words with operators
    question = question.replace("multiplied by","*").replace("divided by","/").replace("plus", "+").replace("minus", "-")
    #Discard 'what is' and '?'
    parts = question.rstrip("?").split()[2:]

    if not parts:
        raise ValueError("syntax error")
    
    operator = "+"
    value = 0
    for index, part in enumerate(parts):
        if not(is_number(part) or part in [ "+", "-", "*", "/"]):
            # You have supplied neither a known operation or a number
            raise ValueError("unknown operation")

        if index % 2: # Every other part of the question must be an integer and the other must be an operator
            if is_number(part):
                # you have supplied a number where an operator should have been
                raise ValueError("syntax error")
            operator = part
        else:
            if not is_number(part):
                # you have supplied an operator where a number should have been
                raise ValueError("syntax error")
            value = perform_operation(value, int(part), operator)
            operator = ""
            
    if operator: # question finished on an operator.
        raise ValueError("syntax error")
    return value


def is_number(string_part: str):
    """Is the number an integer
    :param string_part: str - input string
    :return: bool - is input an integer """
    return string_part.isdigit() or string_part[0] == "-" and len(string_part)>1 and string_part[1:].isdigit


def perform_operation(value_1: float, value_2: int, operator: str):
    """Perform the operation between value_1 and value_2
    :param value_1: float - the value on the left side of the operation
    :param value_2: int - the value on the right side of the operation
    :param operation: bool - the operation to be performed"""
    if operator == "+":
        return value_1 + value_2
    if operator == "-":
        return value_1 - value_2
    if operator == "/":
        return value_1 / value_2
    # operator must be *
    return value_1 * value_2
