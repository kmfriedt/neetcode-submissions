class LRUNode():
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value # this is the value we want to return 
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache_map = dict() # value = node_ptr)
        self.max_capacity = capacity
        self.current_capacity = 0
        self.lru_head = LRUNode(0, 0)
        self.lru_tail = LRUNode(0, 0)
        self.lru_head.next = self.lru_tail
        self.lru_tail.prev = self.lru_head

    def get(self, key: int) -> int:
        if key in self.cache_map:
            node = self.cache_map[key]
            # need to update so this key is the most recently used
            self.remove(node)
            self.insert(node)
            return node.value

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache_map:
            # check the capacity
            if self.current_capacity == self.max_capacity:
                # at capacity then we evict the LRU
                node = self.lru_tail.prev
                self.remove(node)
                # remove it from the cache
                self.cache_map.pop(node.key, None)
            else:
                # under capacity then we add it to the cache_map
                self.current_capacity += 1
            # now we add the node
            node = LRUNode(key, value)
            self.cache_map[key] = node
            # update it so it is the most recently used
            self.insert(node)
        else:
            # update the value
            node = self.cache_map[key]
            node.value = value
            # update it so it is the most recently used
            self.remove(node)
            self.insert(node)
        

    def remove(self, node: LRUNode):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        node.next = node.prev = None


    def insert(self, node: LRUNode):
        prev, nxt = self.lru_head, self.lru_head.next
        prev.next = node
        node.prev = prev
        nxt.prev = node
        node.next = nxt




