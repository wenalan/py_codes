# 144. Binary Tree Preorder Traversal

# standard solution
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        s = [root]
        while s:
            curr = s.pop()
            res.append(curr.val)
            if curr.right:
                s.append(curr.right)
            if curr.left:
                s.append(curr.left)
        return res


# O(1) space traversal
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []

        res = []
        while root:
            if not root.left:
                res.append(root.val)
                root = root.right
            else:
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right
                if prev.right:
                    prev.right = None
                    root = root.right
                else:
                    prev.right = root
                    res.append(root.val)
                    root = root.left
        return res


# recursion with helper function
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        def impl(root, res):
            if not root: return
            res.append(root.val)
            impl(root.left, res)
            impl(root.right, res)

        res = []
        impl(root, res)
        return res


# recursion
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val] + left + right


