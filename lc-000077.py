class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        """
            2024-05-20

            Better solution with some notes explaining how we're traversing partial solution tree
        """


        res = []
        def search(i, combo):
            if len(combo) == k:
                res.append(combo.copy())
            else:
                for j in range(i, n + 1):
                    # Include j and continue trying to add a number in  j + 1, ...; or j + 2, ... or j+ 3, .... etc.
                    search(j + 1, combo + [j])

        search(1, [])
        return res

        """

            Idea:
            - "Process" with increasingly shorter suffix arrays, we only add elements to the _right_ of current element
            - Let the recursion deal with "nesting the appropriate number of loops" (in this case k loops)
            - watch out for off by one errors
        """

        res = []
        def search(start, combo):
            if len(combo) == k: 
                res.append(combo.copy())
                return 

            for i in range(start, n + 1): 
                # Try adding only elements to the _right_ of start - 1
                combo.append(i)
                search(i + 1, combo)
                combo.pop()

        search(1, [])
        return res
        