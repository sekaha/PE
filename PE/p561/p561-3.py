from itertools import accumulate


# Exponent of highest power of 2 dividing n https://oeis.org/A007814
def v2(n):
    return (n & -n).bit_length() - 1


def Q(n):
    m = 904961
    res = 0
    arr = []
    arr2 = []

    # Lifting the exponent lemma v_p(x^n-y^n) = v_p(x-y)+v_p(n)
    for i in range(1, n + 1):
        if i % 2 == 0:
            a = (i + 2) // 2
            res += v2(a - 1)
            arr.append(v2(a - 1))
        else:
            a = (i + 1) // 2
            res += v2(a)
            arr2.append(v2(a))

    print(" ".join(map(str, accumulate(arr))))
    print(" ".join(map(str, accumulate(arr2))))

    return res


print(Q(100))
