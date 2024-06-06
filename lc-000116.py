
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]': 
       
        """
            2024-06-06

            Hmm, I'm not sure why this isn't working. I think it's some issue with frontiers?
            EDIT: It's because you forgot to return the root. 
        
        """
        
        if not root: return

        frontier = []
        frontier.append(root)
        while frontier: 
            
            for i in range(len(frontier)): 
                frontier[i].next = frontier[i + 1] if i < len(frontier) - 1 else None 
            
            # Populate for next level that needs processing
            next_frontier = []  
            for node in frontier: 
                if node.left: next_frontier.append(node.left)
                if node.right: next_frontier.append(node.right)
            frontier = next_frontier
        
        return root 
            