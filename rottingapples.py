import numpy as np
class Solution:
    def orangesRotting(self, grid) -> int:
        fresh = 0
        m, n = len(grid), len(grid[0])
        q = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] ==  2:
                    q.add((i, j))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        while q:
            tmp = set()
            for curx, cury in q:
                for dirx, diry in directions:
                    tx, ty = curx + dirx, cury + diry
                    if 0 <= tx < m and 0 <= ty < n and grid[tx][ty] == 1:
                        tmp.add((tx, ty))
                        grid[tx][ty] = 2    
            q = tmp
            if q:
                res += 1
                fresh -= len(q)
        
        return res if fresh == 0 else -1
val=Solution()
n=int(input())
R=n
C=n
entries = list(map(int, input().split())) 
matrix = np.array(entries).reshape(R, C)
print(val.orangesRotting(matrix))
