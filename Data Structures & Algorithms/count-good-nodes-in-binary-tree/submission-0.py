# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_val):
            if not node:
                return 0
            
            # 1. Is the current node "good" ?
            # It is good if its value is greater than or equal to the max seen so far
            good = 1 if node.val >= max_val else 0

            # 2. Update the max value for the children
            # The children will need to know the highest value on the path 
            curr_max = max(max_val, node.val)

            # 3. Recursively check the left and right branche and add their good nodes
            good += dfs(node.left, curr_max)
            good += dfs(node.right, curr_max)

            return good

        return dfs(root, root.val)

