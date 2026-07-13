class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # output is in any order
        # the output is always unique
        result = list()
        # create a map of the occurrances (bucket)
        bucket_map = defaultdict(list)
        # create a map of the frequencies
        freq_map = defaultdict(int)
        # highest frequecny
        max_freq = 0
        for num in nums:
            # update the freq_map
            freq_map[num] += 1
            # update the max freq
            if freq_map[num] > max_freq:
                max_freq = freq_map[num]
            # update the bucket_map
            # we use the frequency of the current num as the value
            # we then add that num to the list of values in the bucket
    
            bucket_map[freq_map[num]].append(num)
        # now start at the max_freq and look in the bucket map for values
        result = set()
        for index in range(max_freq, -1, -1):
            # add the values in this bucket to the result
            for num in bucket_map[index]:
                result.add(num)
            # add the values to the result while len(result) < k
            if len(result) == k:
                return list(result)
            if len(result) > k:
                print(f"we found an error at index: {index} values: {bucket_map[index]}")
          


