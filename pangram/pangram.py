"""Function for determining pangrams"""
def is_pangram(sentence: str):
    """Determine if sentence is pangram
    
    :param sentece str: A sentence
    :return bool: Is sentence a pangram
    Determines if sentence is a pangram
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz" 
    return all(char in sentence.lower() for char in alphabet)