""" functions for determining the answer to a mathematical question formulated in plain english"""

operator_dict = {
    "multiplied by": "__mul__",
    "divided by": "__truediv__",
    "plus": "__add__",
    "minus": "__sub__"
}
operators = operator_dict.values()


def answer(question:str):
    """ Evaluate the result of a mathematical question formulated in plain english
    :param question: str - a question
    :return: float - the answer to the question
    The method works by 
    1) Cleaning up the question
    2) Validate the question
    3) Calculate the result
    """
    question = clean_question(question)
    parts = question.split()
    validate_question(parts)
    return perform_calculations(parts)


def clean_question(question: str):
    """cleans up the question so that only the essential part is left
    :param question: str - A question
    :return: str - the clean up question"""
    question = question.removeprefix("What is").removesuffix("?").strip()
    for plain_english, operator in operator_dict.items():
        question = question.replace(plain_english,operator)
    return question


def is_number(part: str):
    """Is the number an integer
    :param string_part: str - input string
    :return: bool - is input an integer"""
    return part.lstrip("-").isdigit()


def validate_question(parts: list[str]):
    """Validates the question
    :param parts: list [str] - the question broken down into parts"""
    if not parts:
        raise ValueError("syntax error")
    
    for index, part in enumerate(parts):
        if not(is_number(part) or part in operators):
            raise ValueError("unknown operation")
        
        # ^ == xor. not(a xor b) => false+false == true, true+true == true, otherwise false
        # The index and is_number must match.
        if not (index % 2 ^ is_number(part)):
            raise ValueError("syntax error")
    
    if len(parts) % 2 != 1:
        raise ValueError("syntax error")


def perform_calculations(parts: list[str]):
    """Performes the calculates to calculate the answer"""
    operator = "__add__"
    value = 0
    for index, part in enumerate(parts):
        if index % 2:
            operator = part
        else:
            value = value.__getattribute__(operator)(int(part))
    return value
