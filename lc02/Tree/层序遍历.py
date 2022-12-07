class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode):

        if not root:
            return []
        res = []  # 作为返回结果 ,它里面还是还是一个列表，其实就是res[temp]
        temp = []
        # q=deque([root])  这一句等同于下面两句话，这也是为什么队列能直接的append，就是因为里面就是一个列表
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            temp.append(node.val)  # 把node加入到结果中去
            # 把左右都加入进来
            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)
        return temp


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
    res = solution.levelOrder(Roots)
    print(res)
