# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        """
            2024-06-06
            Level order traversal with explicit tracking of frontiers
            (basically you're BFSing a tree)
        
        """

        level_order = []
        if not root: return []
        frontier = [root]
        while frontier:
            vals = [ node.val for node in frontier ]
            level_order.append(vals)

            next_frontier = [] 
            for node in frontier: 
                if node.left: next_frontier.append(node.left)
                if node.right: next_frontier.append(node.right)

            frontier = next_frontier

        return level_order
        