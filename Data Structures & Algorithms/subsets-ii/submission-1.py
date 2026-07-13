class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = list()
        subset = list()
        nums.sort()
        def dfs(i):
            # base case
            if i >= len(nums):
                subsets.append(subset.copy())
                return
            # include the value at i
            subset.append(nums[i])
            dfs(i+1)
            # clean up the subset to exculde value at i
            subset.pop()
            # recursive call on the next index that is not the same as i
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1) 



        dfs(0)
        return subsets