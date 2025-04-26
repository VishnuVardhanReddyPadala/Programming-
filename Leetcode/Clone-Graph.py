class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        
        clone_map = {}
        
        def dfs(node):
            if node in clone_map:
                return clone_map[node]
            
            clone_node = Node(node.val)
            clone_map[node] = clone_node
            
            for neighbor in node.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
            
            return clone_node
        
        return dfs(node)