class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        #
        #
        #   Slightly improved solution using for loops
        #
        #

        n = len(nums)
        subsets = []

        for bitstring in range(2 ** n):
            subset = []
            for shift in range(n):
                if bitstring & 1 << shift:
                    subset.append(nums[shift])

            subsets.append(subset)
        return subsets
        #
        #
        #   A solution using bit strings to pick out which elements!
        #   - avoids use of stack/recursion so you don't get overflow
        #
        #   Comes from counting how many subsets there are in a set
        #   Either chose ith or don't  so 2 ^ n possible choices
        #
        n = len(nums)
        subsets = []
        for bitstring in range(2 ** n):

            subset = []
            j = 0b1
            idx = 0
            while idx < n:
                if j & bitstring:
                    subset.append(nums[idx])
                j = j << 1
                idx += 1

            subsets.append(subset)


        return subsets

        #
        #
        #   Iterative solution by DFSing with a stack
        #
        #

        ## TODO:

        #
        #   Recursive solution using DFS
        #
        #

        n = len(nums)
        subsets = []

        # Variable for creating a subset
        curr = []
        def dfs(level):
            if level >= n:
                # We've made decisions to include/exclude every element
                # - so here is a possible subset, add to "scribble pad"
                subsets.append(curr.copy())
                return
            
            # This encodes the bifurcating along the tree for generating subsets
            # and is where backtracking is happening
            curr.append(nums[level])
            dfs(level + 1)

            curr.pop() 
            dfs(level + 1)
            
        dfs(0)
        return subsets