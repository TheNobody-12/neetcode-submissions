# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p,q):

            if p is None and q is None:
                return True
            
            if p is None or q is None:
                return False

            if p.val != q.val:
                return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        # 2. Base cases for the main search
        # An empty subRoot is technically a subtree of any tree
        if subRoot is None:
            return True
        # If root is empty but subRoot is not, we can't possibly find it
        if root is None:
            return False

        # 3. Check if the trees match starting at the current 'root' node
        if sameTree(root, subRoot):
            return True

        # 4. If they don't match, keep searching down the left OR right branches
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        