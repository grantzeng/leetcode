class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
            O(n) solution is honestly kind of baffling, go look up a proof. It's not remotely clear to me 
            why we can just do this in a single pass.
        """

        """
            First attempt at brute force 
            O(n^2) - so times out on big inputs
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
                