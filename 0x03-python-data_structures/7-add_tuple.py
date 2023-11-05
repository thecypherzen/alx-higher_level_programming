#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds up two tuples

    Parameters:
        @tuple_a: the first tuple
        @tuple_b: the second tuple

    Return:
        A tuple whose elements are a sum of corresponding elements in
        each tuple
        - if one tuple has less elments, it is

    """
    if tuple_a is None and tuple_b is not None:
        return tuple_b
    if tuple_a is not None and tuple_b is None:
        return tuple_a
    if tuple_a is None and tuple_b is None:
        return None
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    first = tuple_a if len_a > len_b else tuple_b
    second = tuple_a if len_a < len_b else tuple_b

    ret = [i for i in first]
    for i in range(len(second)):
        ret[i] += second[i]
    return tuple(ret)
