#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """A function that divides element by element 2 lists.

    Parameters:
        @my_list_1: the first list
        @my_list_2: the second list
        @list_length: length of list

    Return:
        a new list (length = list_length) with all divisions

    Description:
        - my_list_1 and my_list_2 can contain any type
            (integer, string, etc.)
        - list_length can be bigger than the length of both lists
        - If 2 elements can't be divided, the division result
            should be equal to 0
        - If an element is not an integer or float:
            print: wrong type
        - If the division can't be done (/0):
            print: division by 0
        - If my_list_1 or my_list_2 is too short
            print: out of range
        - Must use try: / except: / finally:
        - Module imports not allowed
    """

    res = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except Exception:
            pass
        finally:
            res.append(div)
    return res
