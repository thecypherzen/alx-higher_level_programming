#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """A function that replaces all occurrences of an element by
        another in a new list.

    Parameters:
        @my_list: the initial list
        @search: the element to replace in the list
        @replace: the new element

    Return:
        The new list
    """
    return [] if not my_list \
        else list(map(lambda x: x if x != search else
                      replace, my_list))
