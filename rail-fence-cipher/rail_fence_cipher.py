"""Functions for en/decoding using rail fence cipher"""
def encode(message: str, number_of_rails: int):
    """Encodes a message using the rail fence cipher
    
    :param message: str - an unencoded message
    :param rails: int - number of rails (on the fence)
    :return: str - an encoded message
    """
    rails = [""]*number_of_rails
    current_rail = 0
    inc_direction = -1
    for c in message:
        rails[current_rail] += c
        current_rail, inc_direction = get_next_rail_and_direction(current_rail, inc_direction, number_of_rails-1)
    return ''.join(rails)


def decode(encoded_message: str, number_of_rails: int):
    """Decodes a message using the rail fence cipher
    
    :param message: str - an encoded message
    :param rails: int - number of rails (on the fence)
    :return: str - an decoded message
 
    Process
    STEP 1 determine how many letters belong to each rail
    # We do this by recreating how the encoding assigns letters to rails, only we just count the number of letters.
    # Starting from rail 0 we add a one to a counter for this rail, then progressing until the last rail and then reversing direction,
    # we do this until we have counted to the number of letters in the encoded message.

    STEP 2 split the encoded message into each rail
    # When we know how many letters go in each rail, we can split our encoded message cleanly into its constituant rails

    STEP 3 decode the message
    # Finally we can decode the message, we do this by read looping back and forth through the rails like in STEP 1,
    # each time we add the first letter in a given rail to the decoded message and eliminating it from the rail.
    """
    # step 1 determine how many letters belong in each rail
    letter_counts = [0]*number_of_rails
    current_rail = 0
    inc_direction = -1
    for dummy in encoded_message:
        letter_counts[current_rail] += 1
        current_rail, inc_direction = get_next_rail_and_direction(current_rail, inc_direction, number_of_rails-1)
    
    # step 2 split encoded message into rails
    rails = []
    chars_transfered = 0
    for row_count in letter_counts:
        rails.append(encoded_message[chars_transfered:chars_transfered+row_count])
        chars_transfered += row_count

    # step 3 decode the message
    decoded_message = ""
    current_rail = 0
    inc_direction = -1
    for dummy in encoded_message:
        decoded_message += rails[current_rail][0]
        rails[current_rail] = rails[current_rail][1:]
        current_rail, inc_direction = get_next_rail_and_direction(current_rail, inc_direction, number_of_rails-1)

    return decoded_message


def get_next_rail_and_direction(current_rail, direction, last_rail):
    """Gets next rail and direction of increment
    
    :param current_rail: str - the current rail
    :param direction: int - the current direction
    :param last_rail: int - the index of the last rail
    :return: int, int - the next rail and the direction of increment
    """
    if current_rail == last_rail or current_rail == 0:
        direction *= -1
    next_rail = current_rail + direction
    return next_rail, direction



print(encode("WEAREDISCOVEREDFLEEATONCE", 3))
print(decode(encode("WEAREDISCOVEREDFLEEATONCE", 3),3))