# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        currentDepth = 0

        if not root:
            return 0
        
        # Recursively get depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Current node's depth = max of children + 1 (for self)
        return max(left_depth, right_depth) + 1

        
            
        