class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
    strs = "abc##d##e##"  # 前序遍历扩展的二叉树序列
    vals = list(strs)
    Roots = Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
    preorder(Roots)

