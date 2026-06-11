class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()
        INF = 2147483647

        # Gathering all the Runners-> 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        dist = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                if grid[r][c] == INF:
                    grid[r][c] = dist
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit and grid[nr][nc] != -1):
                        visit.add((nr,nc))
                        q.append((nr,nc))
                        
            dist+=1
                    

                    
