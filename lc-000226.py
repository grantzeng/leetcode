# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
    
        def invert(curr):  
            if not curr: 
                return 

            invert(curr.left), invert(curr.right)
            curr.left, curr.right = curr.right, curr.left
            
        invert(root)
        return root