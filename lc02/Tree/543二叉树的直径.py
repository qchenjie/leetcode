class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        self.maxDepth(root)
        return self.ans

    # DFS 后序遍历 递归
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0

        leftMaxDepth = self.maxDepth(root.left)
        rightMaxDepth = self.maxDepth(root.right)

        self.ans = max(self.ans, leftMaxDepth + rightMaxDepth)

        return max(leftMaxDepth, rightMaxDepth) + 1


def Creat_Tree(Root, vals):
    if len(vals) == 0:
        return Root
    if vals[0] != '#':  # 本层需要干的就是构建Root、Root.lchild、Root.rchild三个节点。
        Root = TreeNode(vals[0])
        vals.pop(0)
        Root.left = Creat_Tree(Root.left, vals)
        Root.right = Creat_Tree(Root.right, vals)
        return Root  # 本次递归要返回给上一次的本层构造好的树的根节点
    else:
        Root = None
        vals.pop(0)
    return Root  # 本次递归要返回给上一次的本层构造好的树的根节点


def preorder(root):  # 前序遍历
    if root is None:
        return
    else:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


if __name__ == '__main__':
    Root = None
    vals = [1, 2, '#', 5, 6, '#', '#', '#', 3, '#', 4, '#', '#']
    Roots = Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
    # preorder(Roots)
    solution = Solution()
    res = solution.diameterOfBinaryTree(Roots)
    print(res)
