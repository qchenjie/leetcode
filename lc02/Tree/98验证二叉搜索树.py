# 这个题目是递归版本的prev的初始化,对比二叉树展开为链表这个题目

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # nonlocal也用不利索干脆用全局变量
        self.is_bst = True
        self.prev = None
        self.dfs(root)
        return self.is_bst

    def dfs(self, node: TreeNode):
        if not node:
            return
        self.dfs(node.left)
        # 左中右，下面的就是本层节点

        if self.prev and node.val < self.prev.val:  # 如果prev不为空而且右边的节点小于根节点
            self.is_bst = False
        self.prev = node  # 这里的精髓就在这个兄弟，这是递归版本的prev的初始化，看看二叉树展开为链表（这个是迭代版本的初始化
        # prev初始化为当前node，下一句就是node.right,而且没有像level+1传进去，就自然的变成了前一个节点了
        self.dfs(node.right)


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
    vals = [5, 1, '#', '#', 4, 3, '#', '#', 6, '#', '#']
    Roots = Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
    # preorder(Roots)
    solution = Solution()
    res = solution.isValidBST(Roots)
    print(res)
