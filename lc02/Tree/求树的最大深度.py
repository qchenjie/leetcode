
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0 # 这里不能只写return,不然就不是数字了兄弟
        left_height =self.maxDepth(root.left)
        right_height =self.maxDepth(root.right)
        return max(left_height,right_height)+1
#
# 方法二:DFS的迭代版本
# class Solution:
#     def maxDepth(self, root) -> int:
#         if not self:
#             return 0  # 这里不能只写return,不然就不是数字了兄弟
#         res = 0  # 返回值
#         stack = list()
#         stack.append([root, 1])
#         while stack:
#             curr_node, curr_level = stack.pop()
#             res = max(res, curr_level)
#             if curr_node.right:
#                 stack.append([curr_node.right, curr_level + 1])
#             if curr_node.left:
#                 stack.append([curr_node.left, curr_level + 1])
#         return res

# 方法三:DFS的递归版本
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         self.ans = 0
#         self._dfs(root, 1)
#         return self.ans
#
#     def _dfs(self, node, level):
#         if not node:
#             return
#         if self.ans < level:
#             self.ans = level
#         self._dfs(node.left, level + 1)
#         self._dfs(node.right, level + 1)


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
    vals = [3, 9, '#', '#', 20, 15, '#', '#', 7, '#', '#']
    Roots = Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
    # preorder(Roots)
    solution = Solution()
    res = solution.maxDepth(Roots)
    print(res)
