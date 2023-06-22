"""Encrypts a text using asbash encryptions"""
def encode(plain_text:str):
    """With atbash there is really little reasom to separate encrypt and decrypt
    this function simply just formats the output in a way that satisfies the design
    requirements of the tests"""
    encrypted_text = atbash_translate(plain_text)
    block_count = len(encrypted_text)//5 + 1
    return ' '.join(encrypted_text[i*5:(i+1)*5] for i in range(block_count)).strip()


def decode(ciphered_text: str):
    """With atbash there is really little reasom to separate encrypt and decrypt"""
    return atbash_translate(ciphered_text)


def atbash_translate(text: str):
    """Encrypts a text using asbash encryptions
    
    :param text: str - input text plaintext or encrypted
    :return: str - encrypted or plaintext
    since atbash encrypting an atbash ecrypted text simply
    returns the original text. a->z->a then encode = decode
    Obviously for the purposes of this test we must format text that is encoded"""
    translated_text = ''.join(a.lower() for a in text if a.isalnum())
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    tebahpla = "zyxwvutsrqponmlkjihgfedcba"
    return translated_text.translate(str.maketrans(alphabet, tebahpla))
