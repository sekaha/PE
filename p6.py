n = 100

sum_squared = (n * (n + 1) / 2) ** 2
sum_of_squares = (n * (n - 1) * (2 * n - 1)) // 6

print(int(sum_squared - sum_of_squares))
