"""List functionality"""
def append(list1: list, list2: list):
    """Appends two lists"""
    return list1 + list2


def concat(lists):
    """Appends a collection of lists"""
    return [elem for list in lists for elem in list]


def filter(function, list: list):
    """Applies a filter to a list in the form of a lambda function"""
    return [elem for elem in list if function(elem)]


def length(list: list):
    """Computes the lenght of a list"""
    return sum(1 for elem in list)


def map(function, list):
    """Applies (lambda) function to each element of list"""
    return [function(elem) for elem in list]


def foldl(function, list, initial):
    """Accumulates list from the left using lambda function"""
    for elem in list:
        initial = function(initial, elem)
    return initial


def foldr(function, list, initial):
    """Accumulates list from the right using lambda function"""
    for elem in reverse(list):
        initial = function(initial, elem)
    return initial


def reverse(list: list):
    """Reverses list"""
    return list[::-1]
