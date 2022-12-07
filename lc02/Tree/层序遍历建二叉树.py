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

    def build_sequence_order(self):
        li = []
        for a in self.val:  # 创建结点
            node = Node(a)
            li.append(node)

        parentNum = len(li) // 2 - 1
        for i in range(parentNum + 1):
            leftIndex = 2 * i + 1
            rightIndex = 2 * i + 2
            li[i].left = li[leftIndex]
            # 判断是否有右结点， 防止数组越界
            if rightIndex < len(li):
                li[i].right = li[rightIndex]
        return li[0]

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


val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# val = list(input())
bitree = Solution(val)
r = bitree.build_sequence_order()
bitree.in_order(r)
chen = map(str, bitree.res)
print(' '.join(chen))
