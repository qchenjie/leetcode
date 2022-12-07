class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0

        return self._dfs(root, [], targetSum)  # 传进去一个空列表

    def _dfs(self, node, parentPathnum, targetSum):
        if not node:
            return 0
        currPathnum = list()  # 每一次递归进去之后都重新定义一个currPathnum,这样就可以每一个节点都有自己的
        targetSumPathnum = 0  # 当前node的有几个路径,这是为了方便下面的返回值用的
        for i in parentPathnum:
            currPathnum.append(node.val + i)
        currPathnum.append(node.val)

        # 更新
        for i in currPathnum:
            if i == targetSum:
                targetSumPathnum += 1

        # 先不要直接考虑参数传什么东西,你先理清楚要干什么

        leftnum = self._dfs(node.left, currPathnum, targetSum)
        rightnum = self._dfs(node.right, currPathnum, targetSum)
        return leftnum + rightnum + targetSumPathnum  # 左边的加上右边的，还得加上当前节点有几个路径


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
    res = solution.binaryTreePaths(Roots)
    print(res)
