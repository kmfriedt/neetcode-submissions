class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # edge cases
        # -1000, 1000, target = 1, sum = 0 too small so move left ptr up
        # -1000, 1000, target = -1, sum = 0 too big so mvoe right ptr down

        # -1000, 0, target = -500, sum = -1000, too small so move left ptr up
        # 0, 2, 996, 999, 1000, target 998
        #   0, 1000 = 1000 too big move right ptr down to 999
        #   0, 999 = 999 too big move right ptr down to 996
        #   0, 996 = 996 too small move left ptr up to 2
        #   2, 996 = 998 right answer
        # return i + 1 and j + 1 because of 1 indexed
        i, j = 0, len(numbers) - 1

        while i < j: # because we don't want to use the same index
            # add the two numbers together
            total = numbers[i] + numbers[j]
            if total == target:
                return [i+1, j+1]
            elif total > target:
                # the total is too big move right ptr down
                j -= 1
            else:
                # the total is too small, move left ptr up
                i += 1
        