class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.loc = [None] * (len(grid) ** 2)

        for y, row in enumerate(self.grid):
            for x, v in enumerate(row):
                self.loc[v] = (x, y)

    def adjacentSum(self, value: int) -> int:
        res = 0
        x, y = self.loc[value]

        if 0 <= y - 1:
            res += self.grid[x][y - 1]

        if 0 <= x - 1:
            res += self.grid[x - 1][y]

        if y + 1 < len(self.grid):
            res += self.grid[x][y + 1]

        if x + 1 < len(self.grid):
            res += self.grid[x + 1][y]

        return res

    def diagonalSum(self, value: int) -> int:
        res = 0
        x, y = self.loc[value]

        if 0 <= y - 1 and 0 <= x - 1:
            res += self.grid[x - 1][y - 1]

        if 0 <= x - 1 and y + 1 < len(self.grid):
            res += self.grid[x - 1][y + 1]

        if x + 1 < len(self.grid) and y + 1 < len(self.grid):
            res += self.grid[x + 1][y + 1]

        if 0 <= y - 1 and x + 1 < len(self.grid):
            res += self.grid[x + 1][y - 1]

        return res


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
