class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)
            
        return root