class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        for i in range(len(nums)):

            value = nums[i]
            index = abs(value) - 1
            if nums[index] < 0:
                # then we have seen this value before
                return abs(value)
            # other wise we have not seen this value
            # set the value at that index to negative
            nums[index] *= -1
            