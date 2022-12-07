"""
二叉树模板，尽量用这种把函数写到class中格式来，  这样就可以和那种核心模式无缝衔接了
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def __init__(self, val):
        self.val = val
        self.res = []

    def build_pre_order(self):
        if not self.val:
            return
        root_val = self.val.pop(0)
        if root_val == "#":
            return None
        root = Node(root_val)
        root.left = self.build_pre_order()
        root.right = self.build_pre_order()
        return root

    def preorder(self, root):  # 前序遍历
        if root is None:
            return
        self.res.append(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def in_order(self, root):
        if root is None:
            return
        self.in_order(root.left)
        self.res.append(root.data)
        self.in_order(root.right)

    def postorder(self, root):  # 后序遍历
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.res.append(root.data)


while True:
    try:
        val = list(input())
        bitree = Solution(val)
        r = bitree.build_pre_order()
        bitree.in_order(r)
        print(' '.join(bitree.res))
    except:
        break
