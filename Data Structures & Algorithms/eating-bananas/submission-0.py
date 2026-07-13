class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        left = 1
        right = max(piles) # O(n)
        min_k = right
        if len(piles) == h:
            return min_k

        while left <= right:
            k = left + (right-left)//2
            total_hours = 0
            for pile in piles: # O(n)
                total_hours += math.ceil(pile / k)

            if total_hours > h:
                # too slow we need to move left up and get the right side
                left = k + 1
            else: # total_hours < h or == h
                # potentially the right answer or potentially too fast
                right = k - 1
                min_k = min(min_k, k)
        
        return min_k