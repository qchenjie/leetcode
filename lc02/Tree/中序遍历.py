class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


# 前序的迭代版本和图的遍历好像啊
# 迭代想要返回上一个节点，就要从栈中pop出来
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []  # 要返回的结果
        stack = []  # 定义一个栈
        curr = root
        # 注意循环的条件：
        while (curr or stack):
            # 循环左边的
            while (curr):
                stack.append(curr)
                curr = curr.left
            nodes = stack.pop()  # 模拟递归用栈回到上一个节点
            res.append(nodes.val)  # 此时一定是最左边的节点
            # 循环右边的,这里很奇妙，要是我写又会写成了上面的循环左边的while
            # 但是其实只要下面一句话就可以了
            curr = nodes.right
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
    vals = [1, 2, 4, '#', '#', 5, '#', '#', 3, '#', '#', ]
    Roots = Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
    # preorder(Roots)
    solution = Solution()
    res = solution.inorderTraversal(Roots)
    print(res)
