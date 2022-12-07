# 简单的删除链表的元素

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def removeElements(self, head, val) -> ListNode:
#         if not head.next:
#             return
#         head.next = self.removeElements(head.next,val)
#         if head.next.val == val:
#             head.next = None
#         return head

class Solution:
    def removeElements(self, head, val) -> ListNode:
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head


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
    nums = [1, 2, 6, 3, 4, 5, 6]
    head = create_linked_list(nums)
    solution = Solution()
    result = solution.removeElements(head, 6)
    print(print_linked_list(result))
