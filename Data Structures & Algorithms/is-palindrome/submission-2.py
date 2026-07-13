class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower()

        s = re.sub(r'[^a-z0-9]', '', s)

        i = 0
        j = len(s) - 1
        while i < j:
            left = s[i]
            right = s[j]
            if left != right:
                print(f"left: {left} right: {right}")
                return False
            i += 1
            j -= 1

        return True