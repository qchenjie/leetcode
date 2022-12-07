# 删除倒数第n个节点

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = dum = ListNode(0, next=head)  # 虚拟头节点
        # 先初始化slow 和fast的位置
        for i in range(n):
            fast = fast.next
        while fast.next:
            fast, head, slow = fast.next, head.next, slow.next
        slow.next = head.next

        return dum.next


# for i in range(n):
#     fast = fast.next
# while fast.next:  # 是否走到尾部节点
#     fast, head, slow = fast.next, head.next, slow.next
# slow.next = head.next


# class Solution:
# def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#     if not head:
#         return
#     length = 1
#     cur = head
#     while cur.next:
#         length += 1
#         cur = cur.next
#         # 处理特殊情况
#     if length == n:
#         if length == 1:
#             return
#         else:
#             return head.next
#     remain = length - n - 1  # 找到它前一个,万一没有前一个呢
#     cur = head      # 复位
#     while remain > 0:
#         cur = cur.next
#         remain -= 1
#     cur.next = cur.next.next
#     return head


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
    result = solution.removeNthFromEnd(head, 2)
    print(print_linked_list(result))
    # print(result)
