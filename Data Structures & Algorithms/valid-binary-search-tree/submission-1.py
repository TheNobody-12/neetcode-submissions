# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, floor, ceiling):
            if not node:
                return True

            if node.val <= floor or node.val >= ceiling:
                return False

            return (validate(node.left,floor, node.val) and validate(node.right,node.val,ceiling))

        return validate(root, -math.inf,math.inf)
