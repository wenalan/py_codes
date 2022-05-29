# standard solution
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        s = [root]
        prev = None
        while s:
            curr = s[-1]
            hasNoChild = True
            if curr.left or curr.right:
                hasNoChild = False
            visited = False
            if prev and (prev == curr.left or prev == curr.right):
                visited = True
            if hasNoChild or visited:
                res.append(curr.val)
                prev = curr
                s.pop()
            else:
                if curr.right:
                    s.append(curr.right)
                if curr.left:
                    s.append(curr.left)
        return res


# O(1) space traversal
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        while root:
            if root.right:
                prev = root.right
                while prev.left and prev.left != root:
                    prev = prev.left
                if prev.left:
                    prev.left = None
                    root = root.left
                else:
                    prev.left = root
                    res.append(root.val)
                    root = root.right
            else:
                res.append(root.val)
                root = root.left
        res.reverse()
        return res


# recursion with helper
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        def impl(root):
            if not root: return
            impl(root.left)
            impl(root.right)
            res.append(root.val)

        res = []
        impl(root)
        return res


# recursion
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        return left + right + [root.val]
