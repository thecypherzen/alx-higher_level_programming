#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds the biggest int in a list

    Parameters:
        @my_list: the list

    Return:
        The biggest int in list if any, None if list is empty or None

    Constraints:
        - Cannot use built in max() func
        - No module import allowed
    """
    if not my_list:
        return None
    listcpy = my_list.copy()
    listcpy.sort(reverse=True)
    return listcpy[0]
