class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        """
            2024-06-09
            In some more compact code
        
        """
        net_costs = [ g - s for g,s in zip(gas, cost)]
        if sum(net_costs) < 0: return -1
        tank, start = 0, 0 
        for i, net_cost in enumerate(net_costs):
            # Add cost of getting to station i and then checking if it's possible
            tank += net_cost
            if tank < 0: 
                # Can't get to station i
                start, tank = i + 1, 0 
        return start
        
        
        """
            2024-06-09
            O(n) solution
            - it's apparent we're doing a lot of extra computation we don't need, but
              not immediately clear where we can save on work. 

            The O(n) solution relies on proofs...and observations on the problem. Not sure 
            how generalisable this is. 

            ... after spending _far_ too much time writing the proof, the solution makes more sense
        
        """
        # Existence check 
        if sum(gas) < sum(cost):
            # From Claim 1b, we know a solution can't exist 
            # - 1a does NOT logically imply 1b, you have to prove the bloody thing!
            return -1
        
        # Looking for a solution 
        # From Claim 3, we know if we have a path on A[i:n], we don't have to check A[:i]
        # - so we don't bother looping back
        tank = 0
        start = 0
        for i in range(len(gas)): 
            tank += gas[i] - cost[i]

            if tank < 0:
                # From Claim 2, we know if we fail at station i, 
                # then we can't possibly start a loop at any station 0 to i
                # So we jump to checking at station i + 1
                start = i + 1 
                tank = 0         
        return start



        """
            2024-06-09
            Try to reimplement brute force solution using two pointers 
            - basically we need to find at least ONE solution where we can do a cycle. 

            Actually it's not obvious at all how you could prove a solution exists if sum(gas) > sum(cost)
            but this was a minor optimization check that Neetcode does at the start. 
        """
        n = len(gas)
        
        for i in range(n): 
            tank = 0 # Initially tank is zero, because we have to fill up at i (and pay cost[i] for the bloody gas, gas ain't cheap man. )
            
            # Question is: can we go from i -> i + 1 -> ... -> k - 1 -> k -> ... -> i
            for j in range(n): 
                k = (i + j) % n 
                tank += gas[k] - cost[k] # Try to travel to k from k - 1 given current tank state

                if tank < 0: 
                    # Not able to travel from station k - 1 to to k, given we start at i
                    break 

            if tank < 0: 
                # This is to with early break if we can't travel from k - 1 to k, starting at i
                # - This is ugly af code, I dislike it immensely
                continue
            else: 
                # Otherwise we found a route we _can_ travel, i.e. by starting at i because the above loop doesn't 
                # terminate early unless there was a link k - 1 -> k that failed.
                return i

        # We tried every starting position and they all failed, so no route possible
        return -1


        
        """
            First attempt at brute force 
            O(n^2) - so times out on big inputs

            - Basically: test if can do cycle from every point. 
            
            O(n) solution is honestly kind of baffling, go look up a proof. It's not remotely clear to me 
            why we can just do this in a single pass, but we will come back to this later
        """
        n = len(gas)
        for start in range(n): 
            tank = 0

            for j in range(n): 
                next = (start + j) % n
                tank += gas[next] - cost[next]
                if tank < 0:
                    break

            if tank >= 0: 
                return start

        return -1
                