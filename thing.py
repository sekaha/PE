def get_k(m, n):
    res = 0

    f = (n + 1) ** m * ((n + 2) ** m - 2**m) // (2**m)

    while f > 1 and f % 2 == 0:
        f //= 2
        res += 1

    return res


b = []
c = []

for f in range(1, 33):
    res = 0
    b.append(f"{f}".ljust(3))

    while f > 1 and f % 2 == 0:
        f //= 2
        res += 1

    c.append(f"{res}".ljust(3))

print("".join(b))
print("".join(c))


header = " " * 10 + "".join([f"{m}".ljust(4) for m in range(1, 20)])
print(header)
print("-" * len(header))
for n in range(1, 20):
    a = [f"n = {n} | ".rjust(10)]

    for m in range(1, 20):
        a.append(f"{get_k(m,n)}".ljust(4))

    print("".join(a))
