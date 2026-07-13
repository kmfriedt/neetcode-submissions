class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        # set up a sliding window
        # set the window up

        l = 0
        
        max_window_size = 0
        freq_map = defaultdict(int)

        for r in range(len(s)):
            freq_map[s[r]] += 1

            while (r-l+1) - max(freq_map.values()) > k:
                freq_map[s[l]] -= 1
                l += 1

            max_window_size = max(max_window_size, r-l+1)

        return max_window_size
