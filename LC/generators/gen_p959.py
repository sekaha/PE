from gentool import *
from random import choice

chars = "  /\\"
W = 30

print(
    lc_format(["".join([choice(chars) for _ in range(W)]) for _ in range(W)]).replace(
        "\\", "\\\\"
    )
)
