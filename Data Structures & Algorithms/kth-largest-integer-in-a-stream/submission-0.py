class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        # build the min heap with heapify O(n)
        heapq.heapify(self.min_heap)
        # while the size is > k we pop the min element
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # return the new kth largest element every call

        # add the val to the min heap
        heapq.heappush(self.min_heap, val)
        # while the size is > k we pop the min element
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        # return the min element (heap is the size of k)
        return self.min_heap[0]
