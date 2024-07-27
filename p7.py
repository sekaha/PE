from math import log


# MR96, p(n) < n (ln n + ln ln n - 1 + 1.8 ln ln n / ln n), n >= 13
def prime_upperbound(n) -> int:
    """Gives the upper bound for where the nth prime could be."""
    return int(n * (log(n) + log(log(n)) - 1 + 1.8 * log(log(n)) / log(n)))


def nth_prime(n):
    """Sieve of Eratosthenes"""
    if n == 1:
        return 2

    upperbound = prime_upperbound(n)
    is_prime = [True] * upperbound
    prime_count = 1
    curr_prime = 2

    while prime_count < n:
        # limit range
        for i in range(curr_prime * 2, upperbound, curr_prime):
            is_prime[i] = False

        # find the next prime
        for i in range(curr_prime + 1, upperbound):
            if is_prime[i]:
                curr_prime = i
                prime_count += 1
                break

    return curr_prime


print(nth_prime(10_001))
