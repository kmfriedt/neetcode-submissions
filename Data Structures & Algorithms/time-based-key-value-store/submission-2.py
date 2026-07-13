class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        '''
            going to do binary search on the list, we know that it will be in
            increasing order

        '''
        ts_value = self.time_map[key]

        if not ts_value:
            return ""
        
        left = 0
        right = len(ts_value) - 1
        # if ts_value[right][0] < timestamp:
        #     return ts_value[right][1] # this is the string assoicated with the greatest time stamp
        if ts_value[left][0] > timestamp:
            return ""
        while left <= right:
            mid = (left+right)//2
            if ts_value[mid][0] == timestamp:
                return ts_value[mid][1]
            elif ts_value[mid][0] < timestamp:
                # then time stamp is in the right side move left up
                left = mid + 1
            else:
                # timestamp is in the left side move right down
                right = mid - 1

        return ts_value[right][1]

