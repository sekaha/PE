from time import time


def Q(n):
    m = 904961
    n >> 1
    bin_carry_sum = n - n.bit_count()
    return bin_carry_sum + bin_carry_sum * m


s = time()
Q(10**12)
end = time() - s
print(end, "seconds to compute")
