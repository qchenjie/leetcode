# 反转链表

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 法一，用递归的来写

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         # 1. 递归终止条件
#         if head is None or head.next is None:
#             return head
#
#         p = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#
#         return p


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dumy = ListNode(0)
        carry = 0  # 这个是进位
        temp = dumy

        # 当不等长的时候
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry

            carry = int(total / 10)  # 这个是进位的数字

            cur = ListNode(total % 10)

            temp.next = cur
            temp = temp.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next


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
    l1 = [2, 4, 3]
    head1 = create_linked_list(l1)
    l2 = [5, 6, 4]
    head2 = create_linked_list(l2)
    solution = Solution()
    result = solution.addTwoNumbers(head1, head2)
    print(print_linked_list(result))
    # print(result)
