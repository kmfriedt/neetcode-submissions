class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 = empty
        # 1 = fresh
        # 2 = rotting

        # fruit around a rotting fruit rots every min
        # how long till there are zero fresh fruits remaining

        # -1 if that state is not possible (so still a 1 in the graph)

        # find a rotting piece of fruit, bfs and count the number of cycles till there is no fresh fruit around
        from collections import deque
        deq = deque()
        ROWS, COLS = len(grid), len(grid[0])
        fresh = set()
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                
        # need to start from multiple spots in the BFS so have more than one coordinate set on the queue
        # need to traverse the whole graph first and get the fresh ones and 
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    deq.append((row, col))
                    visited.add((row,col))
                elif grid[row][col] == 1:
                    fresh.add((row,col))

        if not fresh:
            return 0

        # now we have the queue built and fresh built
        total_time = 0
        while deq:
            total_time += 1
            for _ in range(len(deq)): # go through the first layer
                row, col = deq.popleft()
                # look at the neighbors and potentially add them to the deq
                for rn, cn in directions:
                    r = row + rn
                    c = col + cn
                    if (
                        r >= 0 and r < ROWS and
                        c >= 0 and c < COLS and
                        (r,c) not in visited and
                        grid[r][c] == 1
                    ):
                        # remove this from fresh
                        if (r,c) in fresh:
                            fresh.remove((r,c))
                        # mark as visited so we don't add it to deq twice
                        visited.add((r,c))
                        # add it to the deq
                        deq.append((r,c))
                        # don't need to update the grid, we only move to 1's and mark them as visited
        
        return total_time - 1 if not fresh else -1

        
        
        
