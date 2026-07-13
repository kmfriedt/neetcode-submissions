class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we have a few different things to track
        # we want to track the numbers in each row
        # we want to track the numbers in each column
        # we want to track the numbers in each box

        # use floor division to get the box key into a tuple
        # use the tuple as the key

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                value = board[row][col]
                if value != ".":
                    if value in rows[row]:
                        return False
                    rows[row].add(value)
                    if value in cols[col]:
                        return False
                    cols[col].add(value)
                    box_key = (row//3, col//3)
                    if value in boxes[box_key]:
                        return False
                    boxes[box_key].add(value)
        return True