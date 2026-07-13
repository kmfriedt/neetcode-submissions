class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        
        while left < right:
            diff = (right - left) // 2 # floor division rounds down in python
            mid = left + diff
            if nums[mid] == target:
                return mid # return the index that we want
            elif nums[mid] < target:
                # if less than target we take the right side
                left = mid + 1 # we already checked mid don't need it
            else:
                # if it is greater than target we take the left side. 
                right = mid - 1

        if nums[left] == target:
            return left
        
        return -1
            