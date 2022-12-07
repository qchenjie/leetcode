
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import deque


class Solution:
    def sortedListToBST(self, head):
        # 找中间节点 ,定义成一个函数
        # 这里找中间节点写成以前的就错了while fast and fast.next纠错了卧槽
        def getMedian(left: ListNode, right: ListNode) -> ListNode:
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def buildTree(left: ListNode, right: ListNode):
            if left == right:  # 数组的是大于，为什么这里是等于,之前数组是mid-1传进去，要是也是等于，如果左边只有一个元素
                # 那left=0,right=mid-1=0那岂不是要跳过左边的元素了，这里既然找不到前一个元素，那就直接传mid，然后改等于
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            # 这里和之前的不同，就不用mid-1，感觉和上面的终止条件有关，之前的
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root

        return buildTree(head, None)

def create_linked_list(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head


if __name__ == '__main__':
    Root = None
    vals = [-10, -3, 0, 5, 9]
    head=create_linked_list(vals)
    solution = Solution()
    res = solution.sortedListToBST(head)
    print(res)
