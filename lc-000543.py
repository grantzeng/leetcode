# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """


        

        """ 
            
            Intuition: 
            - diameter is a global property of a tree -> global variable? 
            - the naive solution is just adding height of left subtree 
              and right subtree but this _assumes_ diameter goes through curr
              but we don't know that!

            Idea is: 
            - helper, while it's dfs-ing, should also update our current
              estimate for diameter, assuming it goes through curr node
            
            - does the height calculation and update to estimate

            Basically a possible naive solution is to: 
            - BFS to get to every node
              - then DFS left and right to find diameter estimate assuming
                diameter gets to curr node 
            but this is a waste of work so you have to figure out how to do
            both the traversal and the additional computation simultaneously

        """

        self.res = 0 

        def helper(curr): 
            if not curr: 
                return 0

            l_height, r_height = helper(curr.left), helper(curr.right)

            # Current estimate for diameter of subtree if must go through curr
            # - if we se a better one, then update the estimate
            diameterCurr = l_height + r_height
            self.res = max(self.res, diameterCurr)

            return 1 + max(l_height, r_height)
        
        helper(root)
        return self.res