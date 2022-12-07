class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.idxMap = {}  # 用一个map维护对应关系,维护的是中序遍历
        for i in range(len(inorder)):
            self.idxMap[inorder[i]] = i
        # 构建这个递归的函数，然后记住这个函数的定义
        self.root_index = 0
        return self.buildTreeNod(0, len(inorder) - 1, preorder, inorder)

    def buildTreeNod(self, left: int, right: int, preorder, inorder) -> TreeNode:

        if left > right:
            return None

        # 构建不需要用到返回值，所以都是写在了前面
        root_val = preorder[self.root_index]
        self.root_index += 1
        root = TreeNode(root_val)
        mid = self.idxMap[root_val]

        # 写成下面那样是不是看不大懂,改成这样就知道了
        # leftNode=buildTree(left, mid - 1)
        # root.right=leftNode
        root.left = self.buildTreeNod(left, mid - 1, preorder, inorder)
        root.right = self.buildTreeNod(mid + 1, right, preorder, inorder)

        return root


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
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    # Roots = Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
    # preorder(Roots)
    solution = Solution()
    solution.buildTree(preorder, inorder)
