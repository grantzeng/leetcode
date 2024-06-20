# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        """
            2024-06-20 
            Neater solution that makes more explicit the two checks we're doing (node existence and value equality)
        """

        if p and q: 
            if p.val == q.val:  return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:               return False
        elif not p and not q:   return True
        else:                   return False

        """
            2024-06-20 
            Working solution

            Basically decision tree is: 
            - Check nodes exist
            - Check values equal 
            
            Then check property is recursively satisfied by left and right children, if both checks passed
        
        """


        if p and q: 
            if p.val == q.val: 
                # Values are same, check left and right children
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else: 
                return False
        else: 
            if not p and not q: # This is not the same as not (p and q) because you could have p, but not q. 
                # Nothing and nothing are "equal" 
                return True 
            else: 
                # But nothing and something are not
                return False




        """
            2024-06-20 

            Broken solution.

            
        """


        
        if p and q: 
            if p.val == q.val: 
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
       
        return False 


        if p and q: 
            if p.val == q.val: 
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else: 
                return False
        else: 
            # Nothing and nothing are "equal" 
            return True

        