# search for integer partitions where
# a+b+c = 1000, a, b < c... a+b <= c
import math


def get_val(n):
    for a in range(1, n):
        for b in range(a + 1, n):
            c = n - a - b

            if math.sqrt(a**2 + b**2) == c:
                return a * b * c


print(get_val(1000))
