class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def toIndex(row, col) -> int:
            # row multiplied by the number of columns
            num_columns = len(matrix[0])
            return (row * num_columns) + col

        def fromIndex(index) -> tuple:
            num_columns = len(matrix[0])
            row = index // num_columns
            col = index % num_columns
            return row, col

        left = 0
        right = toIndex(len(matrix)-1, len(matrix[0])-1)

        while left <= right:
            mid = left + ((right-left)//2)
            row, col = fromIndex(mid)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                # need the right hand side so move left up
                left = mid + 1
            else:
                # need the left hand side
                right = mid - 1

        return False
