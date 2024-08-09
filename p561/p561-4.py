from time import perf_counter


def Q(n):
    m = 904961
    n >> 1
    bin_carry_sum = n - n.bit_count()
    return bin_carry_sum + bin_carry_sum * m


s = perf_counter()
Q(10**12)
end = perf_counter() - s

print(end, "seconds to compute")
