#!/usr/bin/python3

"""A simple calculator app.

Usage:
    ./100-my_calculator.py a operator b
Variables:
    a: first operand
    b: second operand
Allowed operators:
    +: addition
    -: subtraction
    *: multiplication
    /: division
Return:
    None.
"""
if __name__ == "__main__":
    import calculator_1 as cal
    import sys
    tot_args = len(sys.argv)
    cmdargs = sys.argv
    if tot_args < 4:
        print("Usage: {} <a> <operator> <b>".format(cmdargs[0]))
        sys.exit(1)
    try:
        opd1 = int(cmdargs[1])
        opd2 = int(cmdargs[3])
        op = cmdargs[2]

        if op == '+':
            res = cal.add(opd1, opd2)
        elif op == '-':
            res = cal.sub(opd1, opd2)
        elif op == '*':
            res = cal.mul(opd1, opd2)
        elif op == '/':
            res = cal.div(opd1, opd2)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        print("{} {} {} = {}".format(opd1, op, opd2, res))
        sys.exit(0)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Use '*' or \\* for multiplication")
    except Exception:
        print("Some unexpected error occured")
    sys.exit(1)
