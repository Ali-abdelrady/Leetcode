# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []
        q = deque([root])
        res = []
        while q :
            max_num = -2**31
            for i in range(len(q)):
                node = q.popleft()
                max_num = max(max_num,node.val)
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            res.append(max_num)
        print(res)
        return res