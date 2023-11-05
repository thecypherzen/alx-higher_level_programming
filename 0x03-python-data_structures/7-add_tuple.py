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
        return tuple(tuple_b[i] for i in range(len(tuple_b)) if i < 2)
    if tuple_a is not None and tuple_b is None:
        return tuple(tuple_a[i] for i in range(len(tuple_a)) if i < 2)
    if tuple_a is None and tuple_b is None:
        return None
    res = []
    for i, j in enumerate(tuple_a):
        if i < 2:
            res.append(j)
    for i, j in enumerate(tuple_b):
        if i < 2:
            if i == len(res):
                res.append(j)
            else:
                res[i] += j
    reslen = len(res)
    while reslen < 2:
        res.append(0)
        reslen = len(res)
    return tuple(res)
