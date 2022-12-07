class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


# # 后续递归
# class Solution:
#     # BFS
#     def sumOfLeftLeaves2(self, root: TreeNode) -> int:
#         return self.postorder(root, root)
#
#     def postorder(self, node: TreeNode, parent: TreeNode) -> int:
#         if not node: return 0
#         if not node.left and not node.right and parent.left == node:
#             return node.val
#         left_leaves_sum = self.postorder(node.left, node)
#         right_leaves_sum = self.postorder(node.right, node)
#         return left_leaves_sum + right_leaves_sum


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
    res = solution.sumOfLeftLeaves2(Roots)
    print(res)
