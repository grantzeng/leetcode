# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:


        """
            2024-06-06
            DFS recursive solution
        
        """

        if not root: return 0  
        if not root.left: return 1 + self.minDepth(root.right)
        if not root.right: return 1 + self.minDepth(root.left)
    
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        

        """
            2024-06-06
            BFS iterative solution

            Trick is to store the depth with the node when you enqueue it so you don't have to deal with 
            the awkwardness of a single variable trying to track levels

        """
        if not root: return 0 

        queue = []
        queue.append((root, 1))
        
        while queue: 
            node, depth = queue.pop(0)

            if not node.left and not node.right: 
                # Current node is a leaf node, so terminate
                return depth 

            # Add all children nodes for further BFSing
            if node.left: queue.append((node.left, depth + 1))
            if node.right: queue.append((node.right, depth + 1))

        
        
        """
            2024-06-06
            Another incorrect BFS implementation 
        
        """

        if not root: return 0 
        queue = []
        queue.append(root)
        min_depth = 0 
        while queue: 
            min_depth += 1
            n = len(queue)
            for i in range(n): 
                x = queue[i]
                if x.left: 
                    queue.append(x.left)
                elif x.right: 
                    queue.append(x.right)
                else: 
                    # Found a leaf node.
                    break 
            queue = queue[n:]
        return min_depth

        """
            2024-06-06
            Incorrect BFS implementation 

        """
        queue = []
        queue.append(root)
        min_depth = 0
        while queue: 
            n = len(queue)
            for i in range(n): 
                x = queue[i]
                if x.left: queue.append(x.left)
                if x.right: queue.append(x.right)
            queue = queue[n:]
            min_depth += 1

        return min_depth
            
        