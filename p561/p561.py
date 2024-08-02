from math import sqrt, log

call = 0


# S
def get_factors(n):
    little = []
    big = []

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            little.append(i)
            big = [(n // i)] + big

    return little + big


# (n choose 2)
def S(n):
    facts = get_factors(n)

    return sum(
        facts[j] % facts[i] == 0
        for i in range(len(facts))
        for j in range(i + 1, len(facts))
    )


# PM
# MR96, p(n) < n (ln n + ln ln n - 1 + 1.8 ln ln n / ln n), n >= 13
def prime_upperbound(n):
    """Gives the upper bound for where the nth prime could be."""
    if n <= 13:
        return n**2

    return int(n * (log(n) + log(log(n)) - 1 + 1.8 * log(log(n)) / log(n)))


def p(m):
    if m == 1:
        return 1

    upperbound = prime_upperbound(m)
    is_prime = [True] * upperbound
    prime_count = 1
    curr_prime = 2
    prod = 2

    while prime_count < m:
        # limit range
        for i in range(curr_prime * 2, upperbound, curr_prime):
            is_prime[i] = False

        # find the next prime
        for i in range(curr_prime + 1, upperbound):
            if is_prime[i]:
                curr_prime = i
                prod *= curr_prime
                prime_count += 1
                break

    return prod


# E(m,n)
def E(m, n):
    global call
    call += 1
    res = 0
    spmn = S(p(m))

    while spmn % 2 == 0:
        spmn //= 2
        res += 1
        print(call)

    return res


def Q(n):
    return sum(E(904961, i) for i in range(1, n + 1))


# print(S(6))
# print(p(2))
# print(E(2, 1))
print(Q(2))  # - 2714886
