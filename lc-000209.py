class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        """

            How this works
            - outer loop computes prefix sum/expands window
            - inner loop subtracts from the prefix sum/contracts window

        """

        i, j = 0, 0
        total = 0
        res = float('inf')

        while j < len(nums):
            total += nums[j]

            while total >= target:
                res = min(j - i + 1, res)
                total -= nums[i]
                i += 1

            j += 1


        return res if res != float('inf') else 0


        """

            Solution is modified prefix sum computing algorithm
            - Basically if "prefix sum" exceeds total, we shrink the left bound until it doesn't
            - It's not "really" a prefix sum, just an accumulation of prefix sum and subtracting all left elements

        """
        n = len(nums)
        res = float('inf') # Not sure if there's a better sentinel but at this point I'm trying to focus on understanding the grow/shrink behaviour
        i = 0
        total = 0
        for j in range(n):
            total += nums[j]
            while total >= target:
                res = min(j - i + 1, res)
                total -= nums[i]
                i += 1

        return res if res != float('inf') else 0

        """
            2024-05-13
            Gave up and tried to understand intuition of how to grow/shrink the window
            - Idea is: j should keep trying to seek out new elements
                       i should be used to push left bound across

            It's a modified prefix sum... we keep trying to prefix sum
            but if prefix sum exceeds total, then try to shrink left bound
            - But rather than maintaining whole prefix sum array, we

            Is this a greedy algorithm? What's the proof that this works?


        """

        n = len(nums)
        res = float('inf') # math.inf? sys.maxsize?

        i, j = 0, 0
        total = 0
        while j < n:
            total += nums[j]
            while total >= target:
                res = min(j - i + 1, res)
                total -= nums[i]
                i += 1
            j += 1

        return res if res != float('inf') else 0


        """
            Trying yet another solution
            - res is initialised incorrectly?
        """
        n = len(nums)
        res = float('inf')

        i, j = 0, 0
        total = 0

        while j < n:
            total += nums[j]

            while total > target:
                res = min(j - i, res)
                total -= nums[i]
                i += 1

            j += 1


        return res if res != float('inf') else 0

        """

            Third iteration of trying to solve this.

            It's only sliding window in the sense that we look at the subarray sum?
            But really we're using two pointers.

            The problem is when to expand the window

        """
        i, j, n = 0, 0, len(nums)
        total = sum(nums[i:j])
        res = float('inf')          # This is fine

        while i <= j and j < n - 1:
            if total < target:
                j += 1
                total += nums[j]
            else:
                res = min(j - i, res)
                total -= nums[i]
                i += 1

        return res if res != float('inf') else 0


        """
            Second solution, realising we only need the array to be geq than target
            so the subarray sum under consideration we only need to consider two cases


        """
        n = len(nums)
        i, j = 0, 0
        res = float('inf')

        total = sum(nums[i:j])
        while i <= j and j < n - 1:
            if total < target:
                j = j + 1
                total += nums[j]
            elif total >= target:
                res = min(j - i, res)
                i, j = i + 1, j + 1

        return res if res != float('inf') else 0

        """
            Initial attempt:
            - Try a variable sized window and we update the sum by adding or removing elements

            Not 100% sure why this is broken
        """

        n = len(nums)
        i, j = 0, 0
        res = float('inf')

        total = sum(nums[i:j])
        while i <= j and j < n - 1:
            if total < target:
                j = j + 1
                total += nums[j]
            elif total > target:
                total -= nums[i]
                i = i + 1
            else:
                res = min(j - i, res)
                i, j = i + 1, j + 1

        return res if res != float('inf') else 0