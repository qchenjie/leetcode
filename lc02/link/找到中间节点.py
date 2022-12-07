# 找到中间节点



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast=head
        if head is None:
            return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


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
    nums = [1, 2, 3, 4, 5]
    head = create_linked_list(nums)
    solution = Solution()
    result = solution.middleNode(head)
    print(print_linked_list(result))
    # print(result)
