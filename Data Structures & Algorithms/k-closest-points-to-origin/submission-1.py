class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # need to create a list with (distance, point)
        min_heap = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            min_heap.append((distance, point))

        # heapify the list
        heapq.heapify(min_heap)
        
        result = []
        # pop the first k elements
        for i in range(k):
            distance, point = heapq.heappop(min_heap)
            result.append(point)

        return result