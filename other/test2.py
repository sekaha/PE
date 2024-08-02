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


n = 64

for i in range(5):
    print(i, get_factor_count(n**i))

# 1 => 1, 1, 1, 1, 1
# 7 => 1, 2, 3, 4, 5
# 4 => 1 3 5 6 9
# 6 => 1, 4, 9, 16, 25
# 16 => 1, 5, 9, 13, 17
# 20 => 1, 6, 15, 28, 45
# 64 => 1, 7, 13, 19, 25
