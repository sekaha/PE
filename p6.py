n = 100


def sum_of_squares(n):
    return sum([i**2 for i in range(1, n + 1)])


print(((n * (n + 1) / 2) ** 2) - sum_of_squares(n))
