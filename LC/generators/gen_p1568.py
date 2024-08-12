from random import choice
from gentool import *

W = 30

lc_printf([[choice([0, 1, 1, 1, 1, 1, 1, 1, 1]) for _ in range(W)] for _ in range(W)])
