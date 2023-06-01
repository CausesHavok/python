""" Functionality for Encrypting strings with rotational chiper"""
def rotate(text:str, key:int):
    """ Encrypts string with rotational chiper
    
    :param text :str - Input text
    :param key :int - number of spaces to rotate text
    :return :str - Encrypted text
    Encryptes input text with a rotational chiper
    """
    output = []
    for char in text:
        ascii_char = ord(char)
        if char.isalpha():
            zeroing_number = 97 if char.islower() else 65
            letter_number = ascii_char - zeroing_number     #Convert from ascii to letters alphabetic position
            newletter_number = (letter_number + key) % 26   #Rotate letter to new alphabetic position
            ascii_char = newletter_number + zeroing_number  #Convect letters alpabetic position to ascii
        output.append(chr(ascii_char))

    return ''.join(output)