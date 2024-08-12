from math import lcm
from itertools import count


def get_range_lcm(n):
    iter = count(start=n, step=n)

    while True:
        candidate = next(iter)
        accept = True

        for p in range(2, 21):
            if candidate % p != 0:
                accept = False
                break

        if accept:
            return candidate


print(get_range_lcm(20), lcm(*range(1, 21)))
