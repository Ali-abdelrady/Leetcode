# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes = []
        n = len(traversal)
        i = 0
        while i < n :
            # count depth (number of '-')
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Extract the number value
            start  = i
            while i < n and traversal[i].isdigit():
                i += 1
            
            value = int(traversal[start : i])
            nodes.append((value,depth))
        
        # Create Root node
        root = TreeNode(nodes[0][0])
        prevDepth = 0
        mp = {0 : root}

        for i in range(1 , len(nodes)):
            value , depth = nodes[i]
            newNode = TreeNode(value)

            if depth > prevDepth:
                mp[depth - 1].left = newNode
            else :
                mp[depth - 1].right = newNode
            
            prevDepth = depth
            mp[depth] = newNode
        
        return root 

