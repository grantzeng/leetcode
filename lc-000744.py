class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        """
            Why does i point at exactly the element that is one greater than target?

            The invariant is that i is set to mid + 1
            - if target _exists_ in the array:
                then at some point, mid will point to it (i.e. letters[mid] = target)
            - if target _doesn't exist_ in the array, but is within the bounds of the array:
              per the check then

            ... yeah come back to this, this seems a bit like a post-hoc rationalisation.
            We'll have to think about it a bit more: being able to explain the `>=` condition
            is important to understanding this algorithm

            Something to do with upper/lower bounding behaviour you'll have to carefully explain later
        """
        if target < letters[0] or target >= letters[-1]: return letters[0]

        i, j = 0, len(letters) - 1

        while i <= j:
            mid = (i + j) // 2
            # if letters[i] <= target and letters[i + 1] > target:
            #     return letters[i + 1]
            if target >= letters[mid]:
                i = mid + 1
            else:
                j = mid - 1

        return letters[i]



        """
            Alternative solution using exclusive upper bonds
            - we have i < j since A[i:i] is an empty array with exclusive upperbounds
        """

        if target < letters[0] or target >= letters[-1]: return letters[0]

        i, j = 0, len(letters)

        while i < j:
            mid = (i + j) // 2
            if target >= letters[mid]:
                # Normal binary search checks if greater than,
                # - It's not letters[i] will actually be the element in question
                i = mid + 1
            else:
                j = mid # since j is exlusive so last element in new search space is at mid -1

        return letters[i]



        """
            Working solution
            - Intuition:
                -  we do the + 1 and - 1 because we've already looked at mid so remaining to
                   search will be on either side of where mid is
                - i <= j since A[i:i] with inclusive indexing is just A[i] i.e. non empty.

        """

        if target < letters[0] or target >= letters[-1]: return letters[0]

        # Treating indexes as pointers so we have to keep them valid
        i, j = 0, len(letters) - 1

        while i <= j:
            mid = (i + j) // 2

            if target >= letters[mid]:
                i = mid + 1
            else:
                j = mid - 1

        return letters[i]


        """
            Yet another broken solution
            - Explain why it's broken:
        """

        i, j = 0, len(letters) - 1

        while i <= j:
            mid = (i + j) // 2
            if ord(target) <= ord(letters[mid]):
                i = mid + 1
            else:
                j = mid - 1


        return letters[i] if i < len(letters) else letters[0]
        """
            Another broken solution
            - Explain why it's broken:

        """

        i, j = 0, len(letters) - 1

        while i < j:
            mid = (i + j) // 2
            if ord(letters[mid]) <= ord(target):
                i = mid + 1
            else:
                j = mid - 1


        # I'm going to guess that the letter we want is at j
        return letters[j] if ord(letters[j]) > ord(target) else letters[0]


        """
            Initial broken solution:
            - Ends up in an infinite loop, plus there's something where
              I'm not 100% sure what happens when it stops

        """
        # Treating indexes as pointers so we have to keep them valid
        i, j = 0, len(letters) - 1

        while i < j:
            mid = (i + j) // 2
            if ord(letters[mid]) < ord(target): 
                #
                i = mid
            else:
                # 
                j = mid - 1


        # I'm going to guess that the letter we want is at j 
        return letters[j] if ord(letters[j]) > ord(target) else letters[0]