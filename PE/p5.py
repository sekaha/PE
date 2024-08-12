# 36, 60
# 60 % 36 = 24
# 36 % 24 = 12
# 24 % 12 = 0
# 12 % 0 =

import math
from random import randint


def gcd(a, b):
    if a < b:
        b, a = a, b

    if b == 0:
        return a

    c = a % b

    return gcd(b, c)


def gcd_of_list(l):
    a, *l = l

    if len(l) == 1:
        b = l.pop()
        return gcd(a, b)

    return gcd(a, gcd_of_list(l))


def lcm(a, b):
    return (a * b) // gcd(a, b)


def lcm_of_list(l):
    a, *l = l

    if len(l) == 1:
        b = l.pop()
        return lcm(a, b)

    return lcm(a, lcm_of_list(l))


print(math.lcm(*[i for i in range(1, 21)]))
