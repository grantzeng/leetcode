class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
            Slightly nicer hash-table solution
            - Pay O(n) space for O(n) time
        """
        diffs = {}
        for i, num in enumerate(nums):
            diff = target - num
            if num in diffs:
                return [i, diffs[num]]
            else:
                diffs[diff] = 1

        """
            More sensible hash-table solution
            - Keep track of differences we've seen so far
        """
        n = len(nums)
        diffs = {}
        for i in range(n):
            diff = target - nums[i]
            if nums[i] in diffs:
                return [i, diffs[nums[i]]]
            else:
                diffs[diff] = i
        
        """
            Broken sorting solution
            - This doesn't work because the sort scrambles up all the indices
            - So you have to pay O(n) space anyway to keep track of them, argh!

            This doesn't work because you're not allowed to use the same element twice
            e.g. [3, 3] as input will return [1, 1] because of the way the original indexes
            are tracked.

            Would be fine if we just had to return elems and not the actual indices!
        """
        original_index = { num: i for i, num in enumerate(nums)}

        nums.sort()

        i, j = 0, len(nums) - 1

        while i < j:
            total = nums[i] + nums[j]
            if total == target:
                return [original_index[nums[i]], original_index[nums[j]]]
            elif total > target:
                j -= 1
            else:
                i += 1


        """
            Brute force solution
            Literally check all C(n, 2) pairs.
            O(n^2)
        """
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1

        """
            Brute force but using for loops to make the iteration more obvious
            - Can probably rewrite as an incomprehensible one liner with a list comprehension but do that later
        """
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

