""" Calculate the secret handshake response to an inpur number"""
def commands(binary_str: str):
    """ Calculate the secret handshake response to an inpur number

    :param binary_str: str - binary representation of a number
    :return: list[str] - the secret handshake response
    """
    handshake_options = ["wink", "double blink", "close your eyes", "jump"]
    handshake_response = []
    for index, elem in enumerate(reversed(binary_str[1:])):
        if elem == "1":
            handshake_response.append(handshake_options[index])

    if binary_str[0]== "1":
        handshake_response.reverse()

    return handshake_response


