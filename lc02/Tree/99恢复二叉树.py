# 这个题目是递归版本的prev的初始化,对比二叉树展开为链表这个题目

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def __init__(self):
        self.x = self.y = self.prev = None

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node) -> None:
            if not node: return
            dfs(node.left)
            if self.prev and node.val < self.prev.val:
                self.y = node
                if not self.x:
                    self.x = self.prev
                else:
                    return
            self.prev = node
            dfs(node.right)

        dfs(root)
        self.x.val, self.y.val = self.y.val, self.x.val


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
    vals = [100, 99, '#', '#', 105, 1, '#', '#', '#']
    Roots = Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
    # preorder(Roots)
    solution = Solution()
    res = solution.recoverTree(Roots)
    print(res)
