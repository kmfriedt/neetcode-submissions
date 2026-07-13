class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        max_area = 0


        def dfs(row, col):

            if (
                row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                grid[row][col] == 0 or 
                (row, col) in visited
            ):
                # this is not part of an island or we have counted it
                return 0

            # this is part of an island and we have not counted it
            total = 1
            visited.add((row,col))
            total += dfs(row-1, col) #up
            total += dfs(row+1, col) #down
            total += dfs(row, col-1) #left
            total += dfs(row, col+1) #right
            return total



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    size = dfs(r, c)
                    # update the max size
                    max_area = max(size, max_area)

        return max_area