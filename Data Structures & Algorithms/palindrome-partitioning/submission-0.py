class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        partitions = list()

        partition = list()
        def is_palindrome(string):
            start, end = 0, len(string)-1

            while start < end:
                if string[start] != string[end]:
                    return False
                start += 1
                end -= 1
            return True


        def dfs(i, j):
            if j >= len(s):
                if i == j:
                    partitions.append(partition.copy())
                return
            # check if the current sub string is a palindrome
            if is_palindrome(s[i:j+1]):
                partition.append(s[i:j+1])
                dfs(j+1, j+1)
                partition.pop()

            dfs(i, j+1)




        dfs(0, 0)

        return partitions

        '''
        Notes

        we want every sub string to be a palindrome

        base case is where we get to the end with all letters as a palindrome

        "aab" you have three options
        "a", "aa", "aab" but only two are palindromes
        so for the valid palindromes you move a head with that added to the partition and the rest
        of the characters as the sub problem



        '''