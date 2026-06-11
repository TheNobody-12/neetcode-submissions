# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum =  -math.inf
        def get_max_gain(node):
            nonlocal max_sum

            if node is None:
                    return 0

            # 1. Get the max gain from the left and right subtreees.
            # if a subtree is negative, we use max(..,o) to ignore it  completely.
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)

            curr_arch_sum = node.val + left_gain + right_gain

            max_sum = max(max_sum, curr_arch_sum)

            return node.val + max(left_gain, right_gain)
            
        get_max_gain(root)
        return max_sum


