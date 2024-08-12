class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # obsevations
        # if we do a DFS/BFS, we can take " " freely
        # for /, we have to split between T+L and B+R.
        # for \, we have to spilt between  T+R B+L 
        # we need 4x the nodes to account for // case
        # DSU -- implement from scratch 
        R, C = len(grid), len(grid[0])

        nodes = [[r*(C*3+1) + c for c in range(C*3+1)] for r in range(R*3+1)]
        parent = [v for r in nodes for v in r]
        rank = [1]*len(nodes)

        # Trim nodes
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == "/":
                    for off in range(4):
                        new_r, new_c = (r+1)*3-off, c*3+off
                        nodes[new_r][new_c] = None
                        parent[new_r*(C*3+1)+new_c] = None
                
                if val == "\\":
                    for off in range(4):
                        new_r, new_c = r*3+off, c*3+off
                        nodes[new_r][new_c] = None
                        parent[new_r*(C*3+1)+new_c] = None

        # DSU
        def union(a,b) -> bool:
            p1, p2 = find(a), find(b)

            if p1 == p2:
                return False

            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1

            parent[p2] = p1
            rank[p1] += rank[p2]

            return True

        def find(n):
            # work way up tree
            if parent[n] != n:
                parent[n] = find(parent[n])

            return parent[n]

        # BFS and merge
        def bfs(r, c, par):
            for r_off, c_off in ((1,0),(-1,0),(0,1),(0,-1)):
                new_r, new_c = r+r_off, c+c_off

                if 0 <= new_r < len(nodes) and 0 <= new_c < len(nodes[0]) and
                    union():
                    pass
                    

        for r in range(R*3+1):
            for c in range(C*3+1):
                bfs(r, c, parent[r*(C*3+1)+c])

        return 0