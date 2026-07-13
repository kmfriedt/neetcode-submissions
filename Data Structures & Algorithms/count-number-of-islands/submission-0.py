class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):
            if (
                row < 0 or
                row >= ROWS or
                col < 0 or
                col >= COLS or
                grid[row][col] != '1'
            ):
                # not a piece of island
                return
            
            # once we find an island piece we can mark that as visited
            grid[row][col] = '2'
            # we then move through the island and make all the land pieces as visited
            # look up, down, left, right from the square

            # up
            dfs(row-1, col) 
            # down
            dfs(row+1, col) 
            # left
            dfs(row, col-1)
            # right
            dfs(row, col+1)
        
        
        # we want to move through the graph
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    # found an island want to do a dfs on it
                    dfs(r,c)
                    # once we have traversed the island we 
                    # increment the island count
                    num_islands += 1
                # go back to moving through the graph to look for more islands

        return num_islands


