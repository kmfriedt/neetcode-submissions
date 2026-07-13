class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # not guaranteed to have an output
        # return an empty list

        # other wise return a list of lists

        result = []
        # want all 3 indexes where they sum to zero
        # same as finding 2 indexes that sum to negative of the other index value

        # looks like the input is not sorted...
        # that makes the problem very hard

        # could use a hash map with the key being the negative sum of all possible indexes
        # then the value would be the two indexes and you would iterate through again
        # to see if you find the correct key where the index isn't in the values associated
        # with that key
        # would be O(n^2)

        # could sort the list first O(nlog(n)) better than O(n^2)
        # how would we do it if it was sorted

        # nums = [-4, -1, -1, 0, 1, 2]

        # we also want to make sure there are not any duplicate triplets
        # so we don't want -4, -1, 0 and -4, -1, 0 as an answer
        # so we want to skip over any duplicates

        # sort to get rid of duplicates
        nums.sort()
        
        i = 0
        while i < (len(nums)-2):
            target = -nums[i]
            # sub problem where we find two numbers that sum to the target
            l, r = i+1, len(nums)-1
            # now just a two pointer problem like 2sum
            while l < r:
                if nums[l] + nums[r] == target:
                    result.append([nums[i], nums[l], nums[r]])
                    # move l up
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    l+=1
                    # move r down
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                # case where we are below target so l is moved up
                elif nums[l] + nums[r] < target:
                    # move l up
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    l+=1
                # caes where we are above target so r is moved down
                else:
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1

            # now we have to advance i
            while i < (len(nums)-2) and nums[i] == nums[i+1]:
                i += 1
            i += 1

        return result

