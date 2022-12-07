class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []  # 要返回的结果
        stack = []  # 定义一个栈
        curr = root

        pre = None  # 记住当前节点的的前一个节点

        # 注意循环的条件，这里和中序的循环是一样的
        while curr or stack:
            # 循环左边的，对比前序的非递归，这里因为root节点要留着兄弟
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if not curr.right or curr.right == pre:  # 当没有右节点或者已经访问过了
                res.append(curr.val)  # 就因为这里写成了stack.append(root.val)，一上午的时间又没了
                pre = curr  # pre第一次实例化
                curr = None  # curr通过下一次pop出来
            else:
                stack.append(curr)
                curr = curr.right
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
    vals = [1, 2, 4,  '#',  '#',  5,  '#',  '#', 3,  '#',  '#',]
    Roots = Creat_Tree(Root, vals)  # Roots就是我们要的二叉树的根节点。
    # preorder(Roots)
    solution = Solution()
    res = solution.postorderTraversal(Roots)
    print(res)
