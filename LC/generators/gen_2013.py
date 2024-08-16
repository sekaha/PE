from math import sqrt
from gentool import *
from random import randint, choice

actions = ["DetectSquares"]
inputs = [[]]
n = 3000
max_coord = int(sqrt(n)) - 1

for _ in range(n):
    actions.append(choice(["add", "count"]))
    inputs.append([[randint(0, max_coord), randint(0, max_coord)]])

lc_copy_debug(inputs)
print()
lc_copy_debug(actions)
