""" Determine Bob's response based on input string """
def response(hey_bob:str):
    """ Determine Bob's response based on input string

    :param hey_bob string: A message for Bob
    :return string: A response from Bob

    Function determines Bob's response from a limited selection based on few but simple rules
    messages with no content -> "Fine. Be that way!"
    questions that are yelled -> "Calm down, I know what I'm doing!"
    questions -> "Sure"
    messages that are yelled -> "Whoa, chill out!"
    anything else -> "Whatever."
    """
    trimmed_hey_bob = hey_bob.strip()
    is_question = trimmed_hey_bob.endswith('?')
    is_yell = trimmed_hey_bob.isupper()
    
    if not trimmed_hey_bob:
        return "Fine. Be that way!"
    if is_question and is_yell:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return "Sure."
    if is_yell:
        return "Whoa, chill out!"

    return "Whatever."
