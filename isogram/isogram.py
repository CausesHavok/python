""" Determines if string is an isogram"""
def is_isogram(string:str):
    """ Determines if string is an isogram

    :param string str: Input text
    :return bool: Is input an isogram
    Determines if the input string is an isogram ie a string where each letter is only contained once
    """
    scrubbed_string = string.replace(' ','').replace('-','').lower()
    return len(scrubbed_string) == len(set(scrubbed_string))