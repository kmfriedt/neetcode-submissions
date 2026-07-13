class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        combos = []
        combo = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                combos.append(combo.copy())
                return
            if total > target or i >= len(candidates):
                return
            combo.append(candidates[i])
            dfs(i+1, total + combo[-1])
            combo.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total)



        dfs(0, 0)


        return combos


        '''

        , 5, 5, 5, 5]
        '''