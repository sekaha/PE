# Naive prefix sum approach
a = [6, 5, 1, 70, -1, 0, 12, 3, 4, -15, 9]

prefix = [a[0]]
for n in a[1:]:
    prefix.append(prefix[-1] + n)

print("Naive prefix sum:", prefix)


# Fenwick Tree (BIT) implementation
def construct_bit(a):
    bi_tree = [0] * (len(a) + 1)  # 1-based indexing
    for i, val in enumerate(a):
        update(i + 1, val, bi_tree)  # 1-based index adjustment
    return bi_tree


def update(index, value, bi_tree):
    while index < len(bi_tree):
        bi_tree[index] += value
        index += index & -index


def get_sum(index, bi_tree):
    total = 0
    while index > 0:
        total += bi_tree[index]
        index -= index & -index
    return total


def get_range_sum(left, right, bi_tree):
    return get_sum(right, bi_tree) - get_sum(left - 1, bi_tree)


# Initialize BIT and calculate sums
bi_tree = construct_bit(a)

print(bi_tree)

# Query range sum for the prefix sum up to index 3 (0-based index, hence range 0 to 3)
print(
    "BIT range sum (0 to 3):", get_range_sum(1, 2, bi_tree)
)  # Convert to 1-based index for BIT
