# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        """
            2024-06-07
            Now with bonus nonsensical list comprehensions
        """

        if not root: return []
        queue = [root]
        res = []

        while queue: 
            res.insert(0, [node.val for node in queue])
            queue = [ child for node in queue for child in (node.left, node.right) if child] 
        
        return res 

        """
            2024-06-07
            
            Working unoptimized solution. 
            - Basically prepend rather than append the values at each level
        """

        if not root: return []
        queue = [root]
        res = []

        while queue: 
            res.insert(0, [node.val for node in queue])

            next_level = []
            for node in queue: 
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)

            queue = next_level 
        
        return res 

        
