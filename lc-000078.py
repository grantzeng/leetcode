class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:

        """
            2024-05-20
            Better solution making the branching in partial solution tree better
            We just want all nodes in partial solution tree
        """


        n = len(nums)
        res = []

        def search(i, subset):
            if i >= n:
                res.append(subset.copy())
                return

            # Either we add i or we don't to the subset
            # but either way we restart search at i + 1
            search(i + 1, subset + [nums[i]])
            search(i + 1, subset)

        search(0, [])
        return res



        """
            Working solution
            - Basically you have to encode the counting logic of
              "we can either add nums[i] or we don't do the subset"
            - and at every recursion call take a snapshot to get all
              2^n subsets

        """
        n = len(nums)

        res = []

        def search(i, subset):
            if i >= n:
                res.append(subset.copy())
                return

            # Either we add nums[i] or we don't to a subset
            subset.append(nums[i])
            search(i + 1, subset)
            subset.pop()
            search(i + 1, subset)

        search(0, [])
        return res


        """
            A broken solution
            - Why is it broken?
        """
        n = len(nums)

        res = []

        def search(i, subset):
            res.append(subset.copy())

            if i > len(nums): # No more elemens to add
                return

            for j in range(i, len(nums)):
                subset.append(nums[i])
                search(i + 1, subset)
                subset.pop()

        search(0, [])
        return res
        """
            Bit string based solution (no need to worry about)

        """
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