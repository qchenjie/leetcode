class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        if not head:
            return

        # 递归终止条件
        if not head.next:
            return head

        # 递归之前先处理一下
        # 快慢指针找到中间节点
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 此时slow就是中间节点，然后标记好，然后断开
        newhead = slow.next
        slow.next = None

        # 递归左边的
        left = self.sortList(head)
        # 递归右边的
        right = self.sortList(newhead)
        return self.mergeTowList(left, right)

    def mergeTowList(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        dumy = ListNode(0)
        temp = dumy
        # 只要
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        # 如果l1还有
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2

        return dumy.next


def create_linked_list(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head


def print_linked_list(list_node):
    if list_node is None:
        return
    last = []
    cur = list_node
    while cur:
        last.append(cur.val)
        cur = cur.next
    return last


if __name__ == '__main__':
    head = [-1, 5, 3, 4, 0]
    head = create_linked_list(head)
    solution = Solution()
    result = solution.sortList(head)
    print(print_linked_list(result))
