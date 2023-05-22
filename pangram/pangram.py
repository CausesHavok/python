"""Function for determining pangrams"""
def is_pangram(sentence: str):
    """Determine if sentence is pangram
    
    :param sentece str: A sentence
    :return bool: Is sentence a pangram
    Determines if sentence is a pangram
    Works by converting both the alphabet and the sentence to a set (unique list of characters) and comparing them
    """
    return set("abcdefghijklmnopqrstuvwxyz").issubset(sentence.lower()) # alternatively return all(char in sentence.lower() for char in alphabet)

