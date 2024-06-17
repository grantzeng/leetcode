class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        """
            2024-06-17

            Conceptually what is going on is: 


            Smallest number we can get is to try to get front of the number to be monontonic increasing 
            e.g. 12345 is the smallest way to arrage these numbers 

            But we only have k deletes, so when we run out, just have to append the rest. 
            Sometimes we might not use all deletes, so need to account for that. 

            e.g. 122223456789  
        
        """

        stack = []
        
        # Two things: 
        # - front of number we want to be monotonic stac
        # - but if we run out of deletes, just add the rest
        for digit in num: 
            while k and stack and stack[-1] > digit: 
                stack.pop()
                k -= 1
            stack.append(digit)

        # Pop from stack for any remaining deletes
        # - this is same a stack = stack[:len(stack) - k] but I'm writing it out explicitly so you see the conceptual 
        # monotonic stack in the front
        for _ in range(k): 
            stack.pop()
        
        # Clean up the stack
        res = "".join(stack)
        res = res.lstrip("0") 
        res = res if res else "0"
    
        return res
        

        """
            2024-06-17
            Trying to figure out the intuition of how the algorithm works 

            Topics: 
            - Greedy
            - Monotonic stack (this tool has come up a lot, but I don't think I _fully_ understand how to use it)


            Greedy intuition: 
            - For each number
                - while the top of stack is geq our number, keep ditching numbers
                - then add our number 
            
            Intuition: 
            - front of our new number should be monotonic increasing, until we run out of numbers we can throw out
        """
        stack = []
        
        # This does two things:  
        # - while available k, keep the stack monotonic increasing (since this will get us the smallest sequence for the front of the number)
        # - if we run out of deletes, just add the rest to the stack
        for digit in num: 
            while k and stack and stack[-1] > digit: 
                stack.pop()
                k -= 1
            stack.append(digit)
        

        # The issue here now is, we might not have used all k deletes so just delete
        res = "".join(stack[:len(stack)-k])
        return str(int(res)) if res else "0"





        """
            2024-06-17
            Haven't looked at this for like a week?

            The intuition behind the algorithm?

            Also your one line spaghetti does't work. 

        """
        s = []

        for n in num: 
            while s and k > 0 and s[-1] > n: 
                k -= 1; s.pop()
            s.append(n)

        return str(int("".join(s[:len(s) - k]))) or "0"



        """
            2024-06-12

            Similar intution to 316 -- "build result" rather than "remove k from final"

        """
    
        
        """
            2024-06-12
            Brute force:

            There are C(n, k) ways to remove k numbers from num. 
            So brute force is O(n^k) or polynomial time

        """
        pass