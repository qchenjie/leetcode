class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
from collections import deque


class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False
        # sum_Node=0 #这里不能是个全局的变量
        # self._dfs(root, sum_Node) 应该直接写成下面这样的,给一个0传进去，
        return self._dfs(root, 0, targetSum)

    def _dfs(self, node, sum_Node, targetSum):
        if not node:
            return False
        # 这里都不用考虑返回值,所以都写在了递归函数的前面

        # 想一想不能每一个节点都看他等不等于targetSum吧
        if node.left == None and node.right == None:
            return sum_Node + node.val == targetSum

        left_has_path_sum = self._dfs(node.left, node.val + sum_Node, targetSum)
        right_has_path_sum = self._dfs(node.right, node.val + sum_Node, targetSum)

        return left_has_path_sum or right_has_path_sum


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
    res = solution.hasPathSum(Roots, 8)
    print(res)
