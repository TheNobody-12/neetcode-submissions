# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height(node):
            if not node:
                return 0


            # Here we get heights of sub tree that goes UP to parent)
            l_height = height(node.left)
            r_height = height(node.right)

            # check it the longest path trought this node is the max so far 
            # path through node = lefth + right_h 
            self.diameter = max(self.diameter, l_height + r_height)

            return max ( l_height, r_height) + 1
        
        height(root)
        return self.diameter



