# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
            2024-06-24 
            A correct solution


            TODO: Implement an interative solution 

            Effectively this is doing a dfs "in parallel" on both trees
        """

        if not root1 or not root2: 
            return root1 or root2 

        root = TreeNode(val= root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
     
        return root
        


        """
            Initial broken solution
        """
        root = TreeNode()

        if root1 and root2: 
            root.val = root1.val + root2.val 
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
        elif root1: 
            val = root1.val 
        elif root2: 
            val = root2.val     
        else: 
            return 
        
        
        return root
        