class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
            Try a solution where upperbound of search space is exclusive
            TODO:
            - Implement where j is _exclusive_ when looking at what slice of A
            - Implement a solution where we dump a sentinel value for comparisons
        """


        """
            Trying an exclusive upperbound

            This doesn't work.

            TODO:
            - Try writing it with exclusive upper bound
            - Try writing it with sentinels

        """
        n = len(nums)
        i, j = 0, n
        while i < j:
            mid = i + (j - i) // 2 # Mentally check edge cases (e.g. i = n - 1, j = n works)

            if mid < n and nums[mid] < nums[mid + 1]:
                i = mid + 1
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                j = mid
            else:
                return mid

        """
            Working solution
            - Basically yeah, whether you choose to update left or right bound
              first is irrelevant, the point is that mid can't be a peak, if it's
              less than either of its neighbours (if the neighbours exist).
              Just arbitrarily and greedily pick whichever one works

        """
        n = len(nums)
        i, j = 0, n - 1

        # This condition needs to be \leq because
        # A[i:i] is a slice with one element because right pointer points to valid
        # element. So an empty array is A[i:j] but j < i.
        while i <= j:

            mid = i + (j - i) // 2 # this trick to keep indexes in bound


            # Whether we shrink on left or right bound of the search space
            # is irrelevant, both work
            if mid < n - 1 and nums[mid] < nums[mid + 1]:
                i = mid + 1
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                j = mid - 1
            else:
                # Found a peak
                return mid


        """
            Try Neetcode's solution but flip around update
            - ignore overflow thing, because I don't see the point?

            Does this handle edge cases?
            - Single element array, two element array
            - When peak is at left or right edge

            Is a nice algorithm because it works without having to check edge cases


            ...somehow flipping around the checks it doens't work?
            - Issue was calculating mid
        """
        n = len(nums)
        i, j = 0, n - 1

        while i <= j:
            mid = (i + (j - i)) // 2

            if mid < n - 1 and nums[mid] < nums[mid + 1]:
                i = mid + 1
            elif mid > 0 and nums[mid] < nums[mid - 1]:
                j = mid - 1
            else:
                # Found a peak
                return mid




        """
            Neetcode's solution:

            Key ideas
            - How do you ensure valid index?

            - How do you decide whether to shrink search space from left or from the right?
                - I'm fairly sure this doesn't matter, the main point is whether or not
                  element at mid is _less_ than either of its neighbours (because if it is,
                  then obviously it can't be a peak)

            - Why do we set to mid +/- 1?
                - We + 1 and  -1, because we've already inspected at mid
                  so need to exclude it from our search space

        """
        i, j = 0, len(nums) - 1


        while i <= j:
            # This is a way of calulating mid but stopping it from overflowing
            # - I don't 100% get why
            mid = (i + (j - i)) // 2

            # Either search from left
            if mid > 0 and nums[mid] < nums[mid - 1]: # Stop index out of bound erroprs
                j = mid - 1
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                i = mid + 1
            else:
                # Found a peak element
                return mid

        """
            Try modified version where we explicitly "extend" array
            at position "-1" and "n" to be negative infinity.

            This doesn't really work either...why?
        """
        n = len(nums) - 1
        i, j = 0, n

        while i < j:
            mid = (i + j) // 2
            a = nums[mid - 1] if mid > 0 else -float('inf')
            b = nums[mid + 1] if mid < n else -float('inf')

            if nums[mid] > a and nums[mid] > b:
                return mid
            elif nums[mid] > nums[i]:
                i = mid + 1
            else:
                j = mid - 1


        """
            Another attempt

            If we do the naive algorithm: discrete local maxima finder
            - Obvious O(n) solution is just having a window of size 3 and filtering.
            Trying another algorithm:


            Idea is we check the window around mid.
            but this only deals with okay case where:
            - mid is in the middle of a long input and we can have a window
                of size 3.

            - Will break if peak is at 0 or n - 1
            - or if input size < 3
        """
        i, j = 0, len(nums) - 1

        while i < j:
            mid = (i + j) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[i]:
                i = mid + 1
            else:
                j = mid - 1


        """
            Initial broken solution

            - This fails because on [1, 2, 3, 1]
                mid = 1 initially, but obviously 1 < 2 and 1 < 2 for i and j


        """
        i, j = 0, len(nums) - 1

        while i < j: 
            mid = (i + j) // 2
            if nums[mid] > nums[i] and nums[mid] > nums[j]:
                return mid
            elif nums[mid] > nums[i]: 
                i = mid + 1
            else: 
                j = mid - 1






        