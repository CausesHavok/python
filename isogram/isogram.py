""" Determines if string is an isogram"""
def is_isogram(string:str):
    """ Determines if string is an isogram

    :param string str: Input text
    :return bool: Is input an isogram
    Determines if the input string is an isogram ie a string where each letter is only contained once
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    unique_letters = set()
    for char in string.lower():
        if char in alphabet:
            if char not in unique_letters:
                unique_letters.add(char)
            else: 
                return False

    return True #try using list compressions more and remove non alpha letters
