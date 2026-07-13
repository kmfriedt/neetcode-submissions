class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen_nums = set()
        visited_nums = set()
        for num in nums:
            seen_nums.add(num)

        # now have all the nums
        max_length = 0
        for num in seen_nums:
            if num not in visited_nums:
                visited_nums.add(num)
                smallest_num = num
                # go backwards
                while smallest_num - 1 in seen_nums:
                    smallest_num = smallest_num - 1
                    visited_nums.add(smallest_num)
                largest_num = num
                while largest_num + 1 in seen_nums:
                    largest_num = largest_num + 1
                    visited_nums.add(largest_num)
                
                max_length = max(max_length, largest_num - smallest_num + 1)

        return max_length

