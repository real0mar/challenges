class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        def dfs(node: TreeNode | None, is_left: bool, length: int) -> int:
            if not node:
                return length - 1

            left_length = dfs(node.left, False, length + 1 if is_left else 1)
            right_length = dfs(node.right, True, length + 1 if not is_left else 1)

            return max(left_length, right_length)

        return dfs(root, False, 0)
