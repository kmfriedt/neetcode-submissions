class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["." for _ in range(n)] for _ in range(n)] # columns are accesed via the positions in the string

        cols = set()
        posDiag = set()
        negDiag = set()
        boards = list()
        
        def backtrack(r):

            # check if r == n then we make a copy
            if r == n:
                board_copy = ["".join(row) for row in board]
                boards.append(board_copy)
                return
            # now we want to go through each col in the row
            for c in range(n):
                if (
                    c not in cols and
                    r+c not in posDiag and
                    r-c+n not in negDiag
                ):
                    # this is a valid spot
                    board[r][c] = "Q"
                    cols.add(c)
                    posDiag.add(r+c)
                    negDiag.add(r-c+n)
                    # recurse on the next row
                    backtrack(r+1)
                    # clean up
                    board[r][c] = "."
                    cols.remove(c)
                    posDiag.remove(r+c)
                    negDiag.remove(r-c+n)


        backtrack(0)
        return boards

        




