class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        import collections
        d = collections.deque()
        d.append(root.left)
        d.append(root.right)
        while d:
            a = d.popleft()  # 注意popleft和pop区别很大啊兄弟
            b = d.popleft()
            # 下面三句话都是上面的递归的终止条件
            # 如果都为空
            if not a and not b:
                return True
            # 如果有一个为空
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            d.append(a.left)
            d.append(b.right)
            d.append(a.right)
            d.append(b.left)
        return True


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


def inorder(root):  # 中序遍历
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def postorder(root):  # 后序遍历
    if root is None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


if __name__ == '__main__':
    Root = None
    # vals = [1, 2, '#', 3, '#', '#', 2, '#', 3, '#', '#']
    # vals = [1, 2, 3, '#', '#', 4, '#', '#', 2, 4, '#', '#', 3, '#', '#']
    vals = [9, -42, '#', 76, '#', 13, '#', '#', -42, 76, '#', 13, '#', '#', '#']
    Roots = Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
    # print("前序遍历")
    # preorder(Roots)
    # print("中序遍历")
    # inorder(Roots)
    # print("后序遍历")
    # postorder(Roots)
    solution = Solution()
    res = solution.isSymmetric(Roots)
    print(res)
