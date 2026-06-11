# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for key, value in enumerate(inorder):
            inorder_map[value] = key

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            
            root_val = preorder[preorder_index]
            preorder_index = preorder_index + 1

            root_node = TreeNode(root_val)

            mid = inorder_map[root_val]

            root_node.left = build(left, mid - 1)
            root_node.right = build(mid + 1, right)

            return root_node

        return build(0, len(inorder) - 1)