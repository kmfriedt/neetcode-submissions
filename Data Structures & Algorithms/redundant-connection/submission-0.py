class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        We can use the Union find algorithm to tell us when a new edge we add creates a cycle
        '''

        # Union Find
        N = len(edges)
        
        # need to set each nodes parent to it's self first
        parent = [i for i in range(N+1)]
        
        # need to set the rank to 1 for each node0
        rank = [1] * (N+1)

        def find(n):
            if n != parent[n]:
                # recursively go up the chain to find the parent
                parent[n] = find(parent[n])
            return parent[n]


        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                # these two have the same parent so these components are already connected
                return False
            # set the parent based on rank
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return True


        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]