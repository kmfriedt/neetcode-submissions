class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # distinct integers list
        # target integer 
        result = list()
        subset = list()

        def dfs(i):
            if sum(subset) == target:
                result.append(subset.copy())
                return
            if sum(subset) > target:
                return

            if i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(i)
            subset.pop()
            dfs(i+1)

        dfs(0)

        return result

