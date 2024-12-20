# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        def reverse_nodes(nodes):
            l,r = 0 , len(nodes) - 1 
            while l < r :
                nodes[l].val,nodes[r].val = nodes[r].val,nodes[l].val 
                l += 1
                r -= 1 
        temp_node = TreeNode(root.val,root.left,root.right)

        q = [root]
        level = 0
        while q:
            if level % 2 != 0 :
                reverse_nodes(q)
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level +=1         
        return root