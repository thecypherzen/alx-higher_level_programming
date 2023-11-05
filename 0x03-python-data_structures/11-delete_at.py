#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes an item from a list at a specified index

    Parameters:
        @my_list: the list
        @idx: the index of member to delete

    Return:
        - Empty list if my_list is None
        - my_list if idx is < 0 or out of range
        - New list with element at idx deleted

    Constraints:
        - Use of pop() not allowed
        - Module imports not allowed
    """
    if my_list is None:
        return None
    lstlen = len(my_list)
    if not lstlen:
        return []
    if idx < 0 or idx >= lstlen:
        return my_list
    del my_list[idx]
    return my_list
