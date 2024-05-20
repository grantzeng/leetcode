class Solution:
    #def permute(self, nums: List[int]) -> List[List[int]]:
    def permute(self, nums):

        """
            2024-05-20
            Better solution that makes it more explicit that at each point in the potential candidate tree
            the search space is a set difference of what's remaining and the element we've added.

        """
        res = []
        nums = set(nums)

        def search(perm, remaining):
            if not remaining: # Exhausted candidates
                res.append(perm)

            for num in remaining:
                search(perm + [num], remaining - set([num]))

        search([], nums)

        return res

        """
            Second attempt
            - Trick is you need to be able to see how permutations could be generate as a tree structure
            - Start with an empty set:
                - pick an element
                
            Time: O(n!) because of the for loop on remaining runs n then n-1, ..., then 1 etc.
            Space: O(n!) since there's n! permutations of a string of length n
        """
        res = []
        nums = set(nums)

        def search(perm, remaining):

            if not remaining:
                res.append(perm.copy())

            for num in remaining:
                perm.append(num)
                search(perm, remaining - set([num]))
                perm.pop()

            # if not remaining:
            #     res.append(perm.copy())
            #     return

        search([], nums)
        print(res)
        return res


        """

            First attempt broken solution

            It's broken because....

        """
        res = []
        n = len(nums)
        nums = set(nums)
        def search(permutation, remaining): 
            if not remaining: 
                res.append(permutation)
                return 
                
            for i, num in enumerate(remaining): 
                permutation.append(num)
                search(permutation, remaining - set([num]))
                permutation.pop()
                search(permutation, remaining) # The issue is this line, because the function repeats its subproblem so infinite recursion
        search([], nums)
        print(res)
        return res

if __name__ == '__main__':
    Solution().permute([1, 2, 3])