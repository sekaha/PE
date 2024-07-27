n = 600_851_475_143

curr = n
factor = 2
max_factor = 2

while factor < (n**0.5):
    if curr % factor == 0:
        max_factor = factor

    while curr % factor == 0:
        curr //= factor

    factor += 1

print(max_factor)
