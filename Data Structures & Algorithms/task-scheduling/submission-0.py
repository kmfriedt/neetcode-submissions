class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        '''
        NOTES

        tasks[i] upper case char (26 options)
        CPU cyle = 1 task
        tasks can be done in any order

        identical tasks must be separated by n CPU cycles

        want the min num of CPU cycles to complete all tasks

        '''

        '''
        EXAMPLE 1

        XXYY n=2
                   0  1    2   3  4
        schedule = X, Y, idle, X, Y
        output = 5

        We should start with the task with the highest number
        So we need to track the number of each task and the number remaining

        X=2, Y=2

        There will be frequent updates so it will be like a stream
        Could use a max heap so the task with the most left goes first

        We will also have to track when the task can run again

        time = 0
        process X
        X left = 1
        next X time = time + n = 0 + 2 + 1 = 3

        Then we want to track which tasks can go next and what the lowest next time is
        again this is like a stream, numerous updates, so we need to use a min heap to see which 
        is the lowest one that can go next. How do we initialize this though

        Could we use a hashmap instead to track the task and the next time it can run?

        '''
        counts = defaultdict(int)

        for task in tasks:
            counts[task] += 1

        max_heap = []
        for k, v in counts.items():
            max_heap.append((-v,k)) # the count and the task

        heapq.heapify(max_heap)

        min_heap = []
        time = 0

        while min_heap or max_heap:
            while min_heap and time >= min_heap[0][0]: # smallest time value
                _, task, remaining = min_heap[0]
                print(f"min pop at {time}: {task}:{remaining}")
                min_heap=min_heap[1:]
                heapq.heappush(max_heap, (remaining, task))

            if max_heap:
                remaining, task = heapq.heappop(max_heap)
                print(f"max pop at {time}: {task}:{remaining}")
                remaining += 1
                if remaining < 0:
                    print(f"put: {task} on min heap remaining:{remaining}")
                    next_time = time + n + 1
                    min_heap.append((next_time, task, remaining))
            
            time += 1

        return time