"""Flattens nested list"""
def flatten(iterable: list):
    """Flattens nested list
    :param iterable: list - nested list/array
    :return: list - flattened array
    Function which recursively calls itself
    everytime it encounteres a list within the input list"""
    flat_array = []
    for elem in iterable:
        if type(elem) == list:
            flat_array.extend(flatten(elem))
        elif elem != None:
            flat_array.append(elem)
    return flat_array
