class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        s = "zxyzxyz"

        answer = 3

        want to track letters we have seen

        want to create a window

        start l and r at 0

        move r ahead while we haven't seen the letter yet

        once we see a duplicate letter we caclulate the window size
        size = r - l

        now we move l ahead till l is on the letter matching r
        then move l ahead one

        continue moving r ahead
        """

        l, r = 0, 0
        max_length = 0
        seen = set()
        while r < len(s):
            if s[r] in seen:
                # we calculate window length
                max_length = max(max_length, r-l)
                # move l ahead
                while l < r and s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
                r += 1
            else:
                seen.add(s[r])
                r += 1
        max_length = max(max_length, r-l)
        return max_length