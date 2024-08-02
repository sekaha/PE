from functools import reduce

digits = []

with open("p8.txt") as f:
    for l in f:
        digits.extend([int(n) for n in l.strip()])


def get_adjacent_product(n):
    max_product = -1

    for i in range(len(digits) - n):
        max_product = max(max_product, reduce(lambda a, b: a * b, digits[i : i + n]))

    return max_product


print(get_adjacent_product(13))
