from math import sqrt, log2, prod


def E(m, n):
    print(n)
    exponents = [n] * m
    print("here 1", len(exponents))
    latent = prod([((e + 1) * (e + 2)) // 2 for e in exponents])
    excess = prod([(e + 1) for e in exponents])
    print("here 2")
    #
    pairs = latent - excess
    k = 0

    while pairs > 1 and pairs % 2 == 0:
        pairs //= 2
        k += 1

    return k


def Q(n):
    return sum([E(904961, i) for i in range(1, n)])


print(E(2, 1))
print(Q(2))
