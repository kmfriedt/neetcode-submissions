class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # store the result
        result = list()
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        # go through the graph for each point
        # do a bfs where you only move to a square if the adjacent square is lower than it

        # if row = 0 then in pacific
        # if col = 0 then in pacific
        # if row = len(heights) - 1 then in atlantic
        # if col = len(heights[0]) - 1 then in atlantic

        # need to track if we have gotten to the atlantic and pacific for each square
        # if we have gotten to both then we add the starting coordinate to the list
        from collections import deque
        
        def bfs(rr, cc):
            pacific = False
            atlantic = False
            deq = deque()
            deq.append((rr,cc))
            visited = set()
            visited.add((rr,cc))
            while deq:
                for _ in range(len(deq)):
                    row, col = deq.popleft()
                    # print(f"r:{row} c:{col}")
                    # see if the coordinates are in either ocean
                    if row == 0 or col == 0:
                        pacific = True
                    if row == ROWS-1 or col == COLS-1:
                        atlantic = True
                    if pacific and atlantic:
                        return True 
                    # now add the potential neighbors
                    for rn, cn in directions:
                        r = row + rn
                        c = col + cn
                        if (
                            r >= 0 and r < ROWS and
                            c >= 0 and c < COLS and
                            heights[r][c] <= heights[row][col] and
                            (r,c) not in visited
                        ):
                            # we can move here and see if the new square is next to the ocean
                            deq.append((r,c))
                            visited.add((r,c))
                
            return False

        # both = bfs(0, 3)
        # print(both)

        # go through each square in the grid

        for row in range(ROWS):
            for col in range(COLS):
                both_oceans = bfs(row, col)
                if both_oceans:
                    result.append([row, col])
                both_oceans = False

        return result