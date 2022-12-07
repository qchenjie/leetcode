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
    def mergeKLists(self, lists) -> ListNode:
        import heapq

        dummy = ListNode(0)
        p = dummy

        head = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))  # 放入值及位置i
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next


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
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    solution = Solution()
    result = solution.mergeKLists(lists)
    print(print_linked_list(result))
    # print(result)
