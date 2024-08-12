def get_factor_count(n):
    factors = 1

    for i in range(2, n):
        exponent = 0
        prime = i

        if n % prime == 0:
            while n % prime == 0:
                n //= prime
                exponent += 1
            factors *= exponent + 1

        # break at last prime factor
        if i * i > n:
            break

    return factors * (1 + (n != 1))


def get_triangular_factors(x):
    if x % 2 == 0:
        return get_factor_count(x // 2) * get_factor_count(x + 1)
    return get_factor_count(x) * get_factor_count((x + 1) // 2)


print(get_triangular_factors(2162160))

i = 1

while (x := get_triangular_factors(i)) < 500:
    i += 1

print(i * (i + 1) // 2 == 76576500)
