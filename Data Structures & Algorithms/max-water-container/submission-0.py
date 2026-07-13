class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # returning a single integer
        # there are always at least two heights
        # height is 0 to 1000, assume 0 holds no water (safe assumption)

        # track the max_area

        max_area = 0

        l = 0
        r = len(heights)-1
        while l < r: 

            left, right = heights[l], heights[r]

            min_height = min(left, right)
            max_area = max(max_area, min_height * (r-l))
            if left < right:
                l += 1
            elif right < left:
                r -= 1
            else:
                r -= 1

        return max_area