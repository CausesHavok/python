"""determines the index of a given value in a given area or raises an value error if value is not present"""
def find(search_list, value):
    """determines the index of a given value in a given area or raises an value error if value is not present"""
    if not search_list or len(search_list)==1 and value != search_list[0]:
        raise ValueError("value not in array")
    middle_index = len(search_list)//2
    middle_value = search_list[middle_index]

    if value == middle_value:
        return middle_index
    if value > middle_value:
        return middle_index + find(search_list[middle_index:], value)
    else:
        return find(search_list[:middle_index], value)
    