# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        """
            2024-06-06
            The obvious solution is just do a normal level order traversal
            and then reverse the resulting list...but I wonder if there's a 
            way of doing it directly. 
        """

        pass