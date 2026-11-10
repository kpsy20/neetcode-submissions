# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def reverse_tree(node):
            if node == None:
                return

            node.left, node.right = node.right, node.left
            reverse_tree(node.left)
            reverse_tree(node.right)
            return node
        
        reverse_tree(root)
        return root