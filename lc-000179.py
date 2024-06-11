class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
            2024-06-12
            The whole nonsensical oneliner. 
            
            - TODO: rewrite in C where you have to deal with your own parsing problems and implementation of the sort
        """
        import functools
        return str(int("".join(sorted(map(str, nums), key=functools.cmp_to_key(lambda a, b: -1 if a + b > b + a else 1)))))

        """
            2024-06-12
            Problem: of strings of zeros...
            - don't deal with parsing ourselves, just use int -> str -> int
        """
        from functools import cmp_to_key 
        return str(
                    int(
                        "".join(
                    sorted(
                        [ str(n) for n in nums ], 
                        key = cmp_to_key(
                            lambda a, b: -1 if a + b < b + a else 1                
                        ),  
                        reverse= True
                    )
                )
            )
        )
        
        """
            2024-06-12

            Yeah Neetcode also runs into the issue of "3" vs "30"vs "34"

            330 vs 303; 334 vs 343; 3034 vs 3430 <-- basically just concat ab or ba and see which one is bigger. 

            It's clear greedy is probably a good choice - just try to stuff the largest
            digits in the most significant positions 

            Trying to shoehorn a comparator function...it's not behaving

        """
        from functools import cmp_to_key
        return "".join(
            sorted(
                [ str(n) for n in nums ], 
                key = cmp_to_key(
                    lambda a, b: -1 if a + b < b + a else 1                
                ),  
                reverse= True
            )
        )
        
        from functools import cmp_to_key
        return "".join(
            sorted(
                map(str, nums), 
                key = cmp_to_key(
                    lambda a, b: -1 if a + b > b + a else 1                
                ),  
                reverse= True
            )
        )
        
        
        """
            2024-06-12

            Idea: "reversed alphabetical sort then join"
            
            Surprisingly this sort of works... but not always
            but the problem is the sort will classify "30 > 3" rather than "3 > 30"
            - custom comparator?

        """
        return "".join(sorted(map(str, nums),reverse=True))