# 这个题目是递归版本的prev的初始化,对比二叉树展开为链表这个题目

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import List


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        idxmap = {}

        def indoer(root):
            if not root:
                return None
            indoer(root.left)
            if root.val not in idxmap:
                idxmap[root.val] = 1
            else:
                idxmap[root.val] += 1
            indoer(root.right)

        indoer(root)
        # 可以写成这样
        # idxmap = sorted(idxmap.items(), key=lambda x: (x[1], x[0]))
        idxmap = sorted(idxmap.items(), key=lambda x: x[1])
        return list(idxmap[-1][1])


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
    vals = [100, 99, '#', '#', 105, 100, '#', '#', '#']
    Roots = Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。

    solution = Solution()
    res = solution.findMode(Roots)
    print(res)
