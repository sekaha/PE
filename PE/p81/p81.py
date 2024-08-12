data = [[int(v) for v in l.split(",")] for l in open("p81.txt")]

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
dp = [[None] * W for _ in range(H)]

# bottom right side base case
dp[-1][-1] = data[-1][-1]


# search
def get_shortest(x, y):
    if dp[y][x] != None:
        return dp[y][x]

    min_dist = float("inf")

    if 0 <= x + 1 < W:
        min_dist = min(min_dist, get_shortest(x + 1, y))

    if 0 <= y + 1 < H:
        min_dist = min(min_dist, get_shortest(x, y + 1))

    dp[y][x] = min_dist + data[y][x]

    return dp[y][x]


for y in range(H):
    get_shortest(0, y)

print(dp[0][0])
