from math import sqrt
from functools import reduce


# S(n) number of pairs of distinct divisors s.t. a | b
def get_factors(n):
    little = []
    big = []

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            little.append(i)

            if n // i != i:
                big = [(n // i)] + big

    return little + big


# (n choose 2)
def S(n):
    facts = get_factors(n)

    # print(facts)

    found = sum(
        facts[j] % facts[i] == 0
        for i in range(len(facts))
        for j in range(i + 1, len(facts))
    )

    return found


def get_prime_factorization(n):
    primes = []
    exponents = []
    i = 2

    while i * i <= n:
        if n % i == 0:
            exponents.append(0)
            primes.append(i)

        while n % i == 0:
            n //= i
            exponents[-1] += 1

        i += 1

    # n itself is a prime
    if n != 1:
        primes.append(n)
        exponents.append(1)

    return primes, exponents


def S2(n):
    primes, exponents = get_prime_factorization(n)

    print(f"{n} =", "x".join([f"{p}^{c}" for p, c in zip(primes, exponents)]))

    latent = reduce(lambda x, y: x * y, [((e + 1) * (e + 2)) // 2 for e in exponents])
    excess = reduce(lambda x, y: x * y, [(e + 1) for e in exponents])

    return latent - excess


print(S(2162160))
print("factors:", S2(2162160))

# for i in range(10):
#     tmp = S(12**i)
#     j = i + 1
#     print(i, tmp, tmp == (j * (j + 1) // 2) ** 5 - j**5)

# for i in range(100):
#    if S(2**i) != (i * (i + 1) // 2):
#        print("bro!")
#        exit(1)
# else:
#    print("gg")
