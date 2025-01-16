# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """ 
        """
            Challenge exercise: Write this in O(V + E) time complexity.
            - I don't believe you grok this question until you can do that

        """

        """
            Attempt 1: 
            Thoughts: 
            - somehow we have to propagate this LCA information back to the root


            Idea: first you have to find p and q. Then you backtrack up to a LCA. 
                When the LCA is found, then all you need to do is return it


            2025-01-16: I can't confidently say I 100% grok this algorithm, so
            come back to it tomorrow
        """

        #
        #  Try to find p, q in the current level
        # 

        if not root: 
            return None 
    
        if root == p or root == q: 
            return root

        #
        # Try to find p, q in children
        #
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Found a potential LCA, so just return it
        if left and right: 
            return root 

        return left if left else right
    

