class Solution:
    #def permute(self, nums: List[int]) -> List[List[int]]:
    def permute(self, nums):

        """
            Second attempt
            - The issue is to a tree representation of permutations

            - Start with an empty set:
                - pick an element
                

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