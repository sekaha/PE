from random import randint

# Veritification prefix
a = [randint(-100, 100) for _ in range(16)]
prefix = [a[0]]

for i in range(1, len(a)):
    prefix.append(prefix[-1] + a[i])

print(prefix)


# Fenwick (1 indexed)
tree = [0] * (len(a) + 1)


def update(i, delta):
    while 0 < i < len(tree):
        tree[i] += delta
        i += i & -i


def query(i):
    ans = 0

    while 0 < i < len(tree):
        ans += tree[i]
        i -= i & -i

    return ans


# ret diff
def range_query(l, r):
    return query(r) - query(l)


def construct_tree(a):
    # Precompute prefix sums
    prefix = [0] * (len(a) + 1)

    for i in range(1, len(a) + 1):
        prefix[i] = prefix[i - 1] + a[i - 1]

    # Remove excess
    for i in range(1, len(a) + 1):
        tree[i] = prefix[i] - prefix[i - (i & -i)]


construct_tree(a)

# Verification
print(prefix[5], query(6))
print(prefix[10] - prefix[5], range_query(6, 11))
