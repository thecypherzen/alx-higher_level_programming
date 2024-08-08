#!/usr/bin/python3
import random
rand = random.SystemRandom()

def gcd(a, b):
    """Greatest Common Divisor Calculator

    Args:
        a(:obj:int): the first number
        b(:obj:int): the second number

    Returns:
        the greatest common divisor of a and b
    """
    x, y = (a, b) if a >= b else (b, a)
    if y == 0:
        return x
    return gcd(y, x % y)

def ps_rand(a, n, c):
    """Pseudo Random Number Generator"""
    return (a ** 2 + c) % n

def abs(n):
    """Gets Absolute value of a number"""
    return n * -1 if n < 0 else n

def pollard_rhos(n):
    """Using the Pollard Rho's Algorithm"""
    if not n % 2:
        return 2
    a = b = rand.randint(1, n - 1)
    c = rand.randint(1, n - 1)
    d = 1
    while d == 1:
        print(f"a: {a:<10} | b: {b:<10} | c: {c:<10}")
        a = ps_rand(a, n, c)
        b = ps_rand(ps_rand(b, n, c), n, c)
        d = gcd(abs(a - b), n)
    return d

def is_prime(n, a):
    """checks if a number is prime

    Uses the Miller Robbin's algorithm
    Steps:
        1. Get k such that n - 1 = (2^k).(m)
            where m = (n - 1) / (2^k)
        2. Pick random number r in range 1 < a < n - 1
        3. For k times, check for compositeness:
    """
    k = 0
    m = n - 1 if n > 0 else 0
    if m:
        while not m & 1:
            k += 1
            m >>= 1
    a = rand.randrange(2, n - 1)
    b = pow(a, m, n)
    if b == 1 or b == -1:
        return True
    for _ in range (k - 1):
        b = pow(b, 2, n)


n = 57
is_prime(n)
#try:
#    factor = pollard_rhos(n)
#    print("========================================\nRESULT:"
#          + f"{n} / {factor} = {n / factor} rem {n % factor}")
#except Exception as e:
#    print (e)
