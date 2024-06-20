class Solution:
    def integerReplacement(self, n: int) -> int:
        """
            TODO: Optimize using bit operations

            TODO: Write out SRTBOT explanation for the DP solution

            TODO: Proof that greedy stays ahead?
        """

        """
            Deal with stopping case

            IDEA: Make the greedy choice when odd (what's the best thing two steps away? since we get an even number either way) 


            Greedily increment or decrement depending on what result two steps away is
            - If we have two evens, prefer the smaller even
            - If we have only one even, prefer the even
            - If odds -> well want the smaller one
            edge case where if we reach 3, it's unambiguously the case that decrement is always better

            Why decrement is always better if n == 3? 
                3 -> 2 -> 1 (decrement, halve)
                3 -> 4 -> 2 -> 1 (increment, halve, halve)
        
        """
     
        steps = 0 
        while n != 1:
            if n % 2 == 0:                                  
                n //= 2
            else: 
                if n == 3:                                  n -= 1      # Edge case where unambiguously better to decrement
                else:
                    op1, op2 = (n + 1) // 2, (n - 1) // 2 
                    if op1 % 2 == 0 and op2 % 2 == 0:       n -= 1      # Prefer option that results in smaller even (since can halve again either way) 
                    elif op1 % 2 == 0:                      n += 1      # Prefer an even (since can halve again)
                    else:                                   n -= 1      # Both are odd, so just prefer whichever one is smaller
            steps += 1

        return steps

        """
            Almost working solution 
            - Issue is stopping case
        """

        steps = 0
        while n != 1: 
            if n % 2 == 0:
                n //= 2         
            else: 
                # If odd...greedily pick whichever increment or decrement results in a smaller even number
                # - Prefer to get even number that halves to an even number
                op1 = (n + 1) // 2
                op2 = (n - 1) // 2

                if op1 % 2 == 0 and op2 % 2 == 0: 
                    # If both are even, then decrement will be smaller
                    n -= 1
                elif op1 % 2 == 0: 
                    # Only increment results in an even number tha halves to an even number
                    n += 1
                else: 
                    # Only decrement results in an even number that halves to an even number or both 
                    # halve to odd numbers (in which case, just pick the smaller one by decrementing)
                    n -= 1
            steps += 1
        
        return steps
        """
            2024-06-20
            Greedy solution
            When odd, need to greedy choose increment or decrement that results in smaller even number 

            Broken: trying to figure out how to code up greedy choice
        """
        steps = 0
        while n != 1: 
            if n % 2 == 0:
                # If even, just halve it
                n //= 2         
            else: 
                
                # If odd...greedily pick whichever increment or decrement results in a smaller even number
                if (n + 1) % 2 == 0 and (n - 1) % 2 == 0: 
                    n -= 1
                else: 
                    n += 1
            steps += 1
        
        return steps