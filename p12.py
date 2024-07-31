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

        if n == 1:
            break

    return factors


n = 500
i = x = 0

while get_factor_count(x) < n:
    x += i
    i += 1

print(x)
