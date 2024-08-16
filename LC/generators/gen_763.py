from gentool import *
from random import randint, choice


def random_rec(i, upper, n):
    for _ in range(n):
        upper = randint(i, upper)

    return upper


s = [""] * 300

for i, c in enumerate("abcdefghijklmnopqrstuvwxyz" * 3):
    start = randint(i, 300)
    s[start] = c
    s[random_rec(start, 300, 3)] = c

lc_copy_debug("".join(s))
