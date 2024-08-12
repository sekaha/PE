data = [[int(v) for v in l.split(",")] for l in open("p82.txt")]

# Test data
# data = [
#     [131, 673, 234, 103, 18],
#     [201, 96, 342, 965, 150],
#     [630, 803, 746, 422, 111],
#     [537, 699, 497, 121, 956],
#     [805, 732, 524, 37, 331],
# ]

W, H = len(data[0]), len(data)

# Can only move down and left
dp_up = [[None] * W for _ in range(H)]
dp_down = [[None] * W for _ in range(H)]

# bottom right side base case
for y in range(H):
    dp_up[y][-1] = data[y][-1]
    dp_down[y][-1] = data[y][-1]


# search
# dir:1 = down, 0 = right, -1 = up
def get_shortest(x, y, dir=0):
    if not (0 <= x < W and 0 <= y < H):
        return float("inf")

    # base cases
    if dir == 0:
        if dp_down[y][x] == None:
            dp_down[y][x] = (
                min(get_shortest(x, y + 1, 1), get_shortest(x + 1, y)) + data[y][x]
            )

        if dp_up[y][x] == None:
            dp_up[y][x] = (
                min(get_shortest(x, y - 1, -1), get_shortest(x + 1, y)) + data[y][x]
            )

        return min(dp_up[y][x], dp_down[y][x])

    if dir == 1:
        if dp_down[y][x] == None:
            dp_down[y][x] = (
                min(get_shortest(x, y + 1, 1), get_shortest(x + 1, y)) + data[y][x]
            )

        return dp_down[y][x]

    if dir == -1:
        if dp_up[y][x] == None:
            dp_up[y][x] = (
                min(get_shortest(x, y - 1, -1), get_shortest(x + 1, y)) + data[y][x]
            )

        return dp_up[y][x]


#  = set((0, 0))
for y in range(H):
    get_shortest(0, y)

print("\n".join(str(r) for r in dp_up))
print("\n".join(str(r) for r in dp_down))


print(min([min(a[0], b[0]) for a, b in zip(dp_up, dp_down)]))
