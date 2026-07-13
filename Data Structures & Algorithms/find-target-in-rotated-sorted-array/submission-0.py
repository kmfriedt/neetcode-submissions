class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        '''
             l     m        r
            [1, 2, 3, 4, 5, 6]
            [2, 3, 4, 5, 6, 1] 
            [3, 4, 5, 6, 1, 2]
            [4, 5, 6, 1, 2, 3]
            
             l     m        r
            [5, 6, 1, 2, 3, 4]
            [6, 1, 2, 3, 4, 5]

             l     m        r  target = 4 (not in here)
            [3, 5, 6, 0, 1, 2]
             
             m
             l  r             target = 4 (not in here)
            [3, 5, 6, 0, 1, 2]

        '''

        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            # check left side
            if nums[left] <= nums[mid]:
                # sorted order
                if target < nums[mid] and target > nums[left]:
                    # target is potentially in left hand side move right down
                    right = mid - 1
                else:
                    # target is not in the left hand side move left up
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                # right side is in sorted order
                if target > nums[mid] and target < nums[right]:
                    # target is in the right hand side move left up
                    left = mid + 1
                else:
                    # target is not in the right hand side move right down
                    right = mid - 1
        

        return -1 