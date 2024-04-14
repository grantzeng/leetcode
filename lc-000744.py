class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:


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