from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


# 下面的代码虽然有问题，但是对我很有启发性
#
# class Solution:
#     def __init__(self):
#         self.ans = 0
#
#     def widthOfBinaryTree(self, root) -> int:
#         if not root:
#             return None
#         self.postorder(root)
#         return self.ans
#
#     def postorder(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#
#         leftMaxDepth = self.postorder(root.left)
#         rightMaxDepth = self.postorder(root.right)
#
#         # 剪枝,这里既有root(你想写在递归函数前面),又有返回值(你想写在递归函数后面)。有root不一定要写前面(后序递归)
#         if root.left == None and rightMaxDepth:
#             return rightMaxDepth + 1
#
#         self.ans = max(self.ans, leftMaxDepth + rightMaxDepth)
#
#         # 本层返回什么
#         # 当都等于0的时候
#         if leftMaxDepth == 0 and rightMaxDepth == 0:
#             return leftMaxDepth + rightMaxDepth + 1
#         # 当左边不等于0，右边等于0的时候
#         if leftMaxDepth != 0 and rightMaxDepth == 0:
#             return leftMaxDepth
#         # 当都不等于0的时候
#         if leftMaxDepth != 0 and rightMaxDepth != 0:
#             return leftMaxDepth + rightMaxDepth
#

# 看一下答案

class Solution:
    def widthOfBinaryTree2(self, root: TreeNode) -> int:
        return self.postorder(root, 0, 1, list(), list())

    def postorder(self, node: TreeNode, level: int, seq_no: int, start: List[int], end: List[int]) -> int:
        if not node:
            return 0
        # 这个梗在二叉树的右视图中也见到过，这里是维护start 和end，不需要返回值,所以写在递归函数前面
        if len(start) == level:
            start.append(seq_no)
            end.append(seq_no)
        else:
            end[level] = seq_no
      # 深搜的标记层数和求二叉树的最小深度中也见过
        left_max_width = self.postorder(node.left, level + 1, 2 * seq_no, start, end)
        right_max_width = self.postorder(node.right, level + 1, 2 * seq_no + 1, start, end)

        curr_max_width = end[level] - start[level] + 1
        return max(curr_max_width, max(left_max_width, right_max_width))


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
    # vals = [1, 2, '#', 5, 6, '#', '#', '#', 3, '#', 4, '#', '#']
    vals = [1, 3, 5, '#', '#', 3, '#', '#', 2, '#', 9, '#', '#']
    Roots = Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
    # preorder(Roots)
    solution = Solution()
    res = solution.widthOfBinaryTree2(Roots)
    print(res)
