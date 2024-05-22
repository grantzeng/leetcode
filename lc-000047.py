class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
            Explanation of why this algorithm works:
            - We're exploring a partial solution tree by bruteforce. The difficulty is coming up with the right tree to avoid duplicates
            Since want subsets -> need to log every node in the partial solution tree
            Since we want to avoid duplicate sets -> partial solution decision making is based on "subset contains ANY NUMBER of a number
            or it doesn't". Hence the needing to sort.
            - Can think of the partial solution tree being trie like ( partial solution is the whole path) or we have a partial solution
              at every node
        """
        nums.sort()

        res = []

        def search(idx, subset):
            res.append(subset.copy())
            if idx >= len(nums):
                return
            else:
                for j in range(idx, len(nums)):
                    if j > idx and nums[j] == nums[j - 1]:
                        continue
                    else:
                        search(j + 1, subset + [nums[j]])

        search(0, [])
        return res

        """
            2024-05-23
            Gave up and looked for a clue.
            The clue is: sort the input.
            - Draw out on paper what's going on if you don't sort the input

            I'm not entirely sure how to avoid traversing duplicates altogether

            Look at Combination Sum II algorithm for how it avoids generating duplicates
            (you need to be able to see the partial solution tree)

            After looking at the video:
            - it looks like a trie.
            - The idea is that each branch point isn't include/exclude a number at position i
              the branch point should be whether we include _any number of nums[i]_ or don't
                - this will remove duplicates since if you had[10, 1, 2, 7, 6, 1]
                    - and you did the tree by include/exclude at position i, you will get a path that goes 1 -> 7
                      somewhere in your tree, and you'll also get a path that goes 7 -> 1 (which is duplicate)

        """
        res = []

        def search(idx, subset):
            if idx >= len(nums):
                res.append(subset.copy())
            else:
                for j in range(idx, len(nums)):
                    if j > idx and nums[j] == nums[j - 1]:
                        continue
                    else:
                        search(j + 1, subset + nums[j])

        search(0, [])
        return res


        """
            2024-05-22
            Naive solution is doing subset 1 algorithm but adding in a check for whether set is already in res
             - but need to think of a better solution where we don't traverse duplicates at all

            This doesn't
        """
        res = []
        def search(idx, subset): 
            if idx >= len(nums): 
                if subset.copy() not in res:
                    res.append(subset.copy()) 
                return
            
            search(idx + 1, subset + [nums[idx]])
            search(idx + 1, subset)
        
        nums.sort()
        search(0, [])
        return res
        