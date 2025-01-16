class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        


        """

            Attempt 2
            - We're still stuck 

            The issue is how do I use logarithms to avoid the situation with the loss of precision in the multiplication 
        """
        adj = defaultdict(list)
    
        for ((u, v), p) in zip(edges, succProb): 
            # This needs to be log, because we need a max heap
            # -0.69 < -0.3 so heappop popping the "smallest in negative sense" is just popping max
            adj[u].append((log(p), v))
            adj[v].append((log(p), u))

        dist = { start_node : log(1)} # p = 1 
        pq = [(log(1), start_node)] 
        visited = set() 
        
        while pq: 
            # Greedily pick the highest probability neighbour
            wt, curr = heapq.heappop(pq)
            
            if curr in visited: 
                continue
            
            visited.add(curr)

            if curr == end_node: 
                # Reached target node
                return exp(dist[curr])

            for (nxt_wt, nxt) in adj[curr]: 
                if nxt in visited: 
                    continue
                
                new_wt = dist[curr] + nxt_wt

                if nxt not in dist or new_wt > dist[nxt]: 
                    dist[nxt] = new_wt
                    heapq.heappush(pq, (nxt_wt, nxt))


        return 0.0











        """

            Attempt 1
            - Another basically wrong solution 

        """
   
        # adj = defaultdict(list)
        
        # for ((u, v), prob) in zip(edges, succProb): 
        #     adj[u].append((v, -1 * math.log(prob))) 

        # # Run Dijkstra's
        # dist = { start_node: 0 }
        # pq = [(0, start_node)]
        # visited = set()

        # while pq: 
        #     curr_dist, curr_node = heapq.heappop(pq)
        #     curr_dist = -1 * curr_dist
            
        #     if curr_node in visited: continue
        #     visited.add(curr_node)

        #     if curr_node == end_node: return math.exp(-1 * curr_dist)

        #     for nxt, wt in adj[curr_node]: 
        #         if nxt in visited: continue 
        #         new_dist = curr_dist + wt

        #         if nxt not in dist or new_dist < dist[nxt]: 
        #             dist[nxt] = new_dist 
        #             heapq.heappush(pq, (-new_dist, nxt))

        # return 0.0


        """   
            Attempt 0
                
            The problem is that Dijkstra's (like most other SSSP algorithms) relies on the 
            the triangle inequality. 

            But the length of a path is a product of weights, not the sum. 
            and in general not true that p(x, z) <= p(x, y) * p(y, z)
        
            but you can take the log....

        """
     
        # adj = defaultdict(list)
        # for ((u, v), wt) in zip(edges, succProb): 
        #     adj[u].append((v, log(wt)))

        # dist = { node:(-float('inf')) for node in range(1, n + 1)} # -inf in log probability is limit of log(0) i.e.     "unreachable"
        # dist[start_node] = 0  # the log of probability of 1 is 0 

        # # Then we can just do Dijkstra's as normal!

        # pq = [(dist[start_node], start_node)] 
        # visited = set()
        # while pq: 
        #     est, u = heapq.heappop(pq)

        #     if u in visited: 
        #         continue 
            
        #     visited.add(u)

        #     for v, wt in adj[u]: 
        #         d = est + wt
        #         if d < dist[v]: 
        #             dist[v] = d 
        #             heapq.heappush(pq, (dist[v], v))
        # return exp(dist[end_node])


        """
        
            Recapping plain Dijkstra's
        """

        dist = {}
        dist[start] = 0 

        pq = [(0, start)]

        visited = set()
