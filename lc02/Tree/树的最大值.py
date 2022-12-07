class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

# 下面的是我写的，有错误，你调试一下就知道了
# class Solution:
#     def largestValues(self, root):
#         if not root:
#             return 0  # 这里不能只写return,不然就不是数字了兄弟
#         res = []
#         res.append(root.val)
#         queue = deque()
#         queue.append(root)
#         while len(queue):
#             size = len(queue)
#
#             for i in range(size):
#                 curr = queue.popleft()
#
#                 if curr.left:
#                     queue.append(curr.left)
#                 if curr.right:
#                     queue.append(curr.right)
#
#                 res.append(self.findlarge(queue))
#
#     def findlarge(self, tempquue):
#         l = list(tempquue)  # 变成列表
#         temp = l[0].val
#         lenth = len(l)
#         for i in range(1, lenth):
#             if l[i].val > temp:
#                 temp = l[i].val
#         return temp
#

class Solution:
    # BFS
    def largestValues1(self, root: TreeNode):
        if not root: return []
        res, queue = [], deque()
        queue.append(root)
        while len(queue):
            size = len(queue)
            max_value = -2**31
            for i in range(size):
                curr = queue.popleft()
                max_value = max(max_value, curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(max_value)

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
    vals = [1, 2, '#', 5, 6, '#', '#', '#', 3, '#', 4, '#', '#']
    Roots = Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
    # preorder(Roots)
    solution = Solution()
    res = solution.largestValues1(Roots)
    print(res)
