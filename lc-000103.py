class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        """
            2024-06-06

            Sensible solution that actually works
        """
        zigzag = []
        if not root: return []
        frontier = [root]
        level = 0 
        while frontier: 

            vals = [node.val for node in (frontier if level % 2 == 0 else reversed(frontier))]
            zigzag.append(vals) 

            next_frontier = []
            for node in frontier: 
                if node.left: next_frontier.append(node.left)
                if node.right: next_frontier.append(node.right)
            frontier = next_frontier
            level += 1

        return zigzag
        
        

        """
            2024-06-06

            Well, we tried to write it with some nonsensical list comprehensions because I'm currently going through 
            a functional programming phase. 

            This is broken. 
        """
        
        if not root: return root

        zigzag = []
        frontier = []
        level = 0 
        while frontier: 
            zigzag.append([node.value for node in (frontier if level % 2 == 0 else reversed(frontier))])
            next_frontier = [ child for node in frontier for child in (node.left, node.right) if child ]
            frontier = next_frontier
            level += 1

        return root
        