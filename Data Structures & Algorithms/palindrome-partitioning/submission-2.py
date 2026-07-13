class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # pre compute all of the palindromes
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                dp[i][i + l - 1] = (s[i] == s[i + l - 1] and
                                    (i + 1 > (i + l - 2) or
                                    dp[i + 1][i + l - 2]))

        res, part = [], []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if dp[i][j]: # check if this is a palindrome
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

        '''
        Notes

        we want every sub string to be a palindrome

        base case is where we get to the end with all letters as a palindrome

        "aab" you have three options
        "a", "aa", "aab" but only two are palindromes
        so for the valid palindromes you move a head with that added to the partition and the rest
        of the characters as the sub problem



        '''