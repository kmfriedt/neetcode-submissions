class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])

        '''
        Notes

        When we find a surrounded region we want to change all the O to X

        When we don't find a surrounded region then we want to leave them as O

        If we are going through the board and we find a none surrounded region we don't want to 
        double visit it. 

        So we should keep a lookup of visited O's that we can't change so we don't look through them twice
        '''
        from collections import deque
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def bfs(row, col):

            deq = deque()
            deq.append((row,col))
            visited.add((row,col))
            surrounded = True
            surrounded_points = list()

            while deq:
                for _ in range(len(deq)):
                    row, col = deq.popleft()
                    # process this location
                    surrounded_points.append((row,col))
                    if (
                        row == 0 or col == 0 or
                        row == ROWS-1 or col == COLS-1
                    ):
                        surrounded = False # these points are not surrounded
                    # update the neighbors
                    for rn, cn in directions:
                        r, c = row + rn, col + cn
                        if (
                            r >= 0 and r < ROWS and
                            c >= 0 and c < COLS and
                            board[r][c] == 'O' and
                            (r,c) not in visited
                        ):
                            # we can add this to the queue and process it
                            deq.append((r,c))
                            # need to add this to visited
                            visited.add((r,c))
                            
            # go over the whole 'island' in this bfs call prevent multiple creations of deq surrounded etc
            if surrounded:
                # now we change the surrounded points to X
                for r, c in surrounded_points:
                    board[r][c] = 'X'





        # loop to go through the entire matrix

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O' and (row,col) not in visited:
                    bfs(row, col)
        
        # we do not return anything

