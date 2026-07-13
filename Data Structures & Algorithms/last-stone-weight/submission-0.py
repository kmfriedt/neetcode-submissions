class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        stones = [stone * -1 for stone in stones]

        heapq.heapify(stones) # max heap effectively

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            z = x - y
            if z < 0:
                heapq.heappush(stones, z)

        if stones:
            return stones[0] * -1
        else:
            return 0