# 94. Binary Tree Inorder Traversal

# standard solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        s = []
        while root or s:
            if root:
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                res.append(root.val)
                root = root.right
        return res


# O(1) space traversal
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        while root:
            if root.left:
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right
                if prev.right:
                    prev.right = None
                    res.append(root.val)
                    root = root.right
                else:
                    prev.right = root
                    root = root.left

            else:
                res.append(root.val)
                root = root.right
        return res


# recursion with helper
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        def impl(root):
            if not root: return
            impl(root.left)
            res.append(root.val)
            impl(root.right)

        res = []
        impl(root)
        return res


# recursion
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + [root.val] + right
