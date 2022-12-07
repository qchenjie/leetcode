class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


# 前序的迭代版本和图的遍历好像啊

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []  # 要返回的结果
        stack = []  # 定义一个栈
        stack.append(root)
        # 注意循环的条件：
        while (stack):
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return res


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
    vals = [1, 2, 4, '#', '#', 5, '#', '#', 3, '#', '#', ]
    Roots = Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
    # preorder(Roots)
    solution = Solution()
    res = solution.preorderTraversal(Roots)
    print(res)
