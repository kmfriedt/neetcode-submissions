class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        visited = set()
        
        
        def board_search(i, r, c):
        # base case
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in visited:
                return False

            if word[i] == board[r][c]:
                if i == len(word)-1:
                    return True
            # not done yet look at the cells around it with the next index[i]
                visited.add((r,c))
                up = board_search(i+1, r-1, c)
                down = board_search(i+1, r+1, c)
                left = board_search(i+1, r, c-1)
                right = board_search(i+1, r, c+1)
                visited.remove((r,c))
                return up or down or left or right
            else:
                return False
        # if you don't find something return false


        # find the first letter
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    # check this out
                    if board_search(0, r, c):
                        return True
        
        return False
        