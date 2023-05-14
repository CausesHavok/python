import secrets
""" Functions for secure comunications using using Diffie-Hellman Exchange"""
def private_key(p):
    """ Create a secure private key using Diffie-Hellman 

    :param p int: A prime number
    :return int: A private key
    
    This function generates the private key as part of a Diffie-Hellman exchange
    """
    return secrets.randbelow(p-2)+2


def public_key(p, g, private):
    """ Create a public key using Diffie-Hellman 

    :param p int: A prime number
    :param g int: The primitive root modulo (also a prime number)
    :param private int: The private key
    :return int: A public key
    
    This function generates the public key as part of a Diffie-Hellman exchange
    """
    return g**private % p


def secret(p, public, private):
    """ Create a shared secret key for the Diffie-Hellman exchange

    :param p int: A prime number
    :param private int: A private key
    :param public int: A public key
    :return int: A secret key
    
    This function generates the secret key as part of a Diffie-Hellman exchange
    """
    return public**private % p
