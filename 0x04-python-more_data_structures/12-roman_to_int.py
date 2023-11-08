#!/usr/bin/python3
def roman_to_int(roman_string):
    """A function to convert a roman numeral to integer

    Parameters:
        @roman_string: the roman numeral

    Return:
        - 0 if @roman_string is not a string or is None
        - the int value of roman_string
    """
    if type(roman_string) is not str or roman_string is None:
        return 0
    intval = 0   # integer value
    lstr = roman_string.lower()
    slen = len(lstr) - 1
    toskip = 0   # to skip iteration or not
    romans = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    for i in range(slen, -1, -1):
        if toskip:
            toskip = 0
            pass
        else:
            # if current digit > next digit, add diff to intval and pass
            # next iteration. Else, add current digit and continue normally
            curr = romans.get(lstr[i], 0)
            if i:
                next = romans.get(lstr[i - 1], 0)
                if curr > next:
                    intval += (curr - next)
                    toskip = 1
                else:
                    intval += curr
            else:
                intval += curr
    return (intval)
