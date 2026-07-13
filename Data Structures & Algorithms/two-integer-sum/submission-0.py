class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # keys will be the numbers and the value will be the index
        index_map = dict()

        for index, num in enumerate(nums):
            if target - num in index_map:
                return [index_map[target-num], index]
            else:
                index_map[num] = index
                
