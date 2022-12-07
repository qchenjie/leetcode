class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return

        left = self.isSymmetric(root.left)
        right = self.isSymmetric(root.right)

        if left is None and right is None:
            return True

        if left == right:
            return True

        return False


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


def inorder(root):  # 中序遍历
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def postorder(root):  # 后序遍历
    if root is None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


if __name__ == '__main__':
    Root = None
    # vals = [1, 2, '#', 3, '#', '#', 2, '#', 3, '#', '#']
    # vals = [1, 2, 3, '#', '#', 4, '#', '#', 2, 4, '#', '#', 3, '#', '#']
    vals = [1, 2, 8, '#', '#', 3, '#', '#', 2, 4, '#', '#', 4, '#', '#']
    Roots = Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
    # print("前序遍历")
    # preorder(Roots)
    # print("中序遍历")
    # inorder(Roots)
    # # print("后序遍历")
    # # postorder(Roots)
    solution = Solution()
    res = solution.isSymmetric(Roots)
    print(res)
