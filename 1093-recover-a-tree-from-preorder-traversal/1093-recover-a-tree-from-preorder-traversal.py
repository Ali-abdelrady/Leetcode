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
        while i < n:
            # Count depth (number of '-')
            depth = 0 
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Extract the number value
            start = i
            while i < n and traversal[i].isdigit():
                i += 1

            value = int(traversal[start:i]) # Convert string Into Number

            nodes.append((value,depth))

        # Craete Root node
        root = TreeNode(nodes[0][0])
        prevDepth = 0 
        lastRoot = {0 : root}
        for i in range(1 , len(nodes)):
            value , depth = nodes[i]
            newNode = TreeNode(value)

            if depth > prevDepth :
                lastRoot[depth - 1].left = newNode
            else: 
                lastRoot[depth - 1].right = newNode
            
            lastRoot[depth] = newNode
            prevDepth = depth

        return root

        