# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
       curr = root

       while curr:
        # if both nodes are greater than the current node, they are both  in the right subtree
        if p.val > curr.val and q.val > curr.val:
            curr = curr.right
        
        # If both nodes are less than the current node, they are both in the left subtree
        elif p.val < curr.val and q.val < curr.val:
            curr = curr.left

        # If one is greater and one is less (or one equals curr), we found the split point!
        # This makes the current node the Lowest Common Ancestor
        else:
            return curr



        


