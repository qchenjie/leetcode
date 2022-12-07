# 删除重复的元素

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 解法1
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if not head:
#             return
#         chen = set()
#         pre = head
#         cur = head.next
#         chen.add(head.val)
#         while cur:
#             if cur.val in chen:
#                 pre.next = cur.next
#             else:
#                 chen.add(cur.val)
#                 pre=pre.next
#             cur=cur.next
#         return head

# 解法2

class Solution:
    def deleteDuplicates(self, head) -> ListNode:
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            head.next = head.next.next
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
    nums = [1, 1, 2, 2, 3, 3, 4, 5]
    head = create_linked_list(nums)
    solution = Solution()
    result = solution.deleteDuplicates(head)
    print(print_linked_list(result))
