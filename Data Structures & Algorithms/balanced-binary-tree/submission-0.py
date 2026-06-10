# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            # Base case: null node has height 0
            if not node:
                return 0
            
            # Check left subtree
            left = check(node.left)
            if left == -1:          # Left is unbalanced, propagate up
                return -1
            
            # Check right subtree
            right = check(node.right)
            if right == -1:         # Right is unbalanced, propagate up
                return -1
            
            # Check balance at CURRENT node
            if abs(left - right) > 1:
                return -1             # Unbalanced!
            
            # Return height of this node to parent
            return max(left, right) + 1
        
        return check(root) != -1