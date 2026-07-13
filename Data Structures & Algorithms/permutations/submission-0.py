class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []

        def dfs(permute, remaining):        
            if len(permute) == len(nums):
                permutations.append(permute.copy())
                return
            for i in range(len(remaining)):
                permute.append(remaining[i])
                dfs(permute, remaining[:i]+remaining[i+1:])
                permute.pop()

        
        dfs([], nums)
        return permutations