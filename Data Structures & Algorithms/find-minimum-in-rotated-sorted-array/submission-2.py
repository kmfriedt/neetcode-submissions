class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if left == right:
                return nums[left]
            # set mid
            m = left + (right - left)//2

            # evaluate left and right
            if nums[right] < nums[left]:
                # the array is not in sorted order
                # we know that the min number is somewhere on the right side
                if left == m:
                    # then there is 1 element in each subarry so the nums[right] is the answer
                    return nums[right]
                elif nums[left] < nums[m]:
                    # then the left hand side is sorted BUT the min is on the right hand side
                    left = m
                elif nums[m] < nums[right]:
                    # we know the right hand side is sorted and the answer is in the right hand side
                    right = m
            else:
                # the array is in sorted order
                return nums[left]
