class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:


        """
            Rewrite with a for loop over the resulting array
            - since we inspect exactly n elements anyhow
            ...Turns out it's not much faster.
        """
        n = len(nums)
        i, j = 0, n - 1
        res = [0] * n

        for k in range(n - 1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                res[k] = nums[i] ** 2
                i = i + 1
            else:
                res[k] = nums[j] ** 2
                j = j - 1

        return res
        """
            Make it even faster by preallocating space
            - Didn't really improve it
        """
        n = len(nums)
        i, j = 0, n - 1
        res = [0] * n
        k = n - 1

        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                res[k] = nums[i] ** 2
                i = i + 1
            else:
                res[k] = nums[j] ** 2
                j = j - 1
            k = k - 1

        return res
        """
            Trick is actually build the sorted list in reverse
            i.e. from highest element to lowest.
            ...you don't need to find the centre...
        """
        n = len(nums)
        i, j = 0, n - 1
        res = []


        while i <= j:
            # This only works because all inputs are integers
            if abs(nums[i]) > abs(nums[j]):
                res.append(nums[i] ** 2)
                i = i + 1
            else:
                res.append(nums[j] ** 2)
                j = j - 1


        return reversed(res)

        """
            First attempt at a two pointer solution
            - It's broken

            Apart from being broken...could just compare absolute
            values of the the numbers (since it seems like all inputs
            are integers, but obviously would break if there was a decimal
            in (0, 1) somewhere)

            Anyhow it was obvious from the start this wasn't going to be the
            "best" solution.
        """
        n = len(nums)
        res = []

        # Search for 'center'
        # - binary search for 0 in the array essentially.
        i, j = 0, len(nums) - 1

        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] > 0:
                j = mid - 1
            else:
                i = mid + 1

        # Then square on the way out
        i, j = i, i
        while 0 <= i < n and 0 <= j < n:
            square_i = nums[i] ** 2
            square_j = nums[j] ** 2

            if square_i >= square_j:
                res.append(square_i)
                i = i - 1
            else:
                res.append(square_j)
                j = j + 1

        # Add the rest. Either left or right side has been exhausted, so add rest
        while i >= 0:
            res.append(nums[i] ** 2)
            i = i - 1

        while j < n:
            res.append(nums[j] ** 2)
            j = j + 1


        return res



        """
            Obiovus code golf solution, but the point is to try
            to solve with two pointers only. (i.e. try to write
            a solution you could implement with things analogous
            whatever's in C)

            Time: O(nlogn) (sort costs O(nlogn) is the bigger cost
            squaring everything only costs O(n)?)
        """
        return sorted([i ** 2 for i in nums ])
        