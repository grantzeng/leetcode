class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


        """
            Things to do: 
            - Convert edge list representation to adjacency list representation (because it's less useless, an edge list is really a mathematician's representation because they never have to do any bloody computations with it)
            - Run Dijkstra's starting at k. 
                - then return max of the distance array
            
            - OPTIMIZATION: Instead of keeping whole distance array, just add the max logic into the Dijkstra's logic

            Recapping why Dijkstra's works. 
            - Basically we relax distance every time we find a violation of the triangle inequality (this fails if we have negative edge
              weights but we don't here) -> converge to true min distance (I can't remember if I've gone through the proof of this before)
                - Greedily visit neighbour closest (since this adds the least distance to path)
            - It's just BFS except we care about edge weights (conceptually BFS is just Dijkstra where all edges weighted 1)
        """
        # Convert edge list representation to adjacency list representation
        adj_list = defaultdict(list)
        for start_node, end_node, weight in times: 
            adj_list[start_node].append((end_node, weight))

        # Upperbound estimate of distances from k to anywhere else is infty 
        # - which we will keep trying to relax 
        estimates = { node:float('inf') for node in range(1, n + 1) }
        estimates[k] = 0

        # Run Dijkstra's to get SSSP distance from k to everywhere else 
        # - Intution is greedy choose the nearest node because this increases path length the least
        priority_queue = [(0, k)]
        visited = set()
        while priority_queue: 
            curr_estimate, node = heapq.heappop(priority_queue)

            if node in visited: continue
            visited.add(node)

            for neighbour, weight in adj_list[node]:
                distance = curr_estimate + weight 
                if distance < estimates[neighbour]: 
                    # Found violation of triangle inequality
                    estimates[neighbour] = distance
                    heapq.heappush(priority_queue, (estimates[neighbour], neighbour))
        
        # Minimum time is bottlenecked by the furthest node
        max_distance = max(estimates.values())
        return max_distance if max_distance < float('inf') else -1