from random import randint

a = list(range(1, 1001))

print(a)

for _ in range(1_000_000):
    s = randint(0, len(a) - 1)
    e = randint(s, len(a) - 1)

    a[s:e] = a[s:e][::-1]

print(a)
