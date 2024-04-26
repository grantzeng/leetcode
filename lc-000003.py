class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
            Basic working solution:
            - but kinda slow because of how I rebuild set every time?

        """
        n = len(s)
        max_length = 0
        
        for i in range(n):
            window = set()
            for char in s[i:]:
                if char in window: break
                window.add(char)
            max_length = max(max_length, len(window))

        return max_length

        """
            Almost works,
            but you already added start character...so maybe don't do that

        """

        n = len(s)
        max_length = 0

        for i, start in enumerate(s):
            window = set([start])
            for char in s[i:]:
                if char in window:
                    break
                window.add(char)
            max_length = max(max_length, len(window))

        return max_length

        """
            Initial attempts:
            - Some strange off by one errors? Not that strang see note below

            - Basically you have a variable sized window, it should
              grow until you find a repeated character, at which point
              you restart the window?

            This algorithm doesn't work because it only restarts the window
            at positions that is a repeated charater
            e.g. for "dvdf" it won't check for any window starting at v!

        """
        window = set()
        max_length = 0 
        
        for char in s: 
            if char in window: 
                window = set()
            window.add(char)
            max_length = max(max_length, len(window))

        return max_length

        # window = set()
        # max_length = 0 
        
        # for char in s: 
        #     if char in window: 
        #         window = set()
        #     max_length = max(max_length, len(window))
        #     window.add(char)

        # return max_length