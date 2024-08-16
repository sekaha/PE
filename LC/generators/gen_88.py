from gentool import *
from random import randint

N = 100

lc_copy_debug(list(sorted([randint(-(10**9), 10**9) for _ in range(N)])) + [0] * N)
lc_copy_debug(list(sorted([randint(-(10**9), 10**9) for _ in range(N)])))
