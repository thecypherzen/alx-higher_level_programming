#!/usr/bin/python3
def weight_average(my_list=[]):
    """A function that calculates weighted averages

    Parameters:
        @my_list: list of integer tuples in the form (score, weight)

    Return:
        0 if list is empty
        The weighted average otherwise
    """
    if not my_list or my_list is None:
        return 0
    sum = 0.0
    tot = 0.0
    weights = list(tupl[0] * tupl[1] for tupl in my_list)
    total = list(tupl[1] for tupl in my_list)
    for i in range(len(my_list)):
        sum += weights[i]
        tot += total[i]
    av = sum / tot
    return av
