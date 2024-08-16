from math import log

# Do a prime factorization and rewrite everything in terms of it


# MR96, p(n) < n (ln n + ln ln n - 1 + 1.8 ln ln n / ln n), n >= 13
def prime_upperbound(n):
    """Gives the upper bound for where the nth prime could be."""
    if n <= 13:
        return n**2

    return int(n * (log(n) + log(log(n)) - 1 + 1.8 * log(log(n)) / log(n)))
