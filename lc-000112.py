# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        """
            2024-06-24
            Working solution

        """
        if not root: 
            return False 

        remaining = targetSum - root.val 

        # This early search termination doesn't work because we're not guaranteed tree only has positive values 
        # if remaining < 0: return False 

        if not root.left and not root.right: 
            # Reached a leaf 
            return remaining == 0 

        # Otherwise keep searching            
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
        
        
        """
            This breaks on the input (tree = [], targetSum = 0)
        """  
        if not root: 
            # Reached a leaf
            return targetSum == 0
        
        if targetSum < 0: 
            # Early terminate since can't reach leaf without exceeding original target
            return False 
        
        remaining = targetSum - root.val 
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
        