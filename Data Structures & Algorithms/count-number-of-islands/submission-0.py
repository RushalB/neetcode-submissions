class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        res = 0

        def bfs(r,c):
            q = deque()
            seen.add((r,c))
            q.append((r,c))

            while q:
                r,c = q.popleft()
                neighbors = [[0,1],[0,-1],[-1,0],[1,0]]
                for n in neighbors:
                    nx,ny  = n
                    rn = r + nx
                    rc = c + ny
                    if 0 <= rn < rows and 0 <= rc < cols and grid[rn][rc] == "1" and (rn,rc) not in seen:
                        q.append((rn,rc))
                        seen.add((rn,rc))




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    bfs(r,c)
                    res +=1
        return res

        