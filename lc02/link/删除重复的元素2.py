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

# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if not head:
#             return head
#         dumy = ListNode(0)
#         dumy.next = head
#         prev = dumy
#         cur = head
#
#         while cur:
#             while cur.next and cur.val == cur.next.val:  # 先找到不是不是重复的元素，想一想要是这里用的是if会咋样
#                 cur = cur.next
#             if prev.next == cur:
#                 prev = prev.next
#             else:
#                 prev.next = cur.next
#
#             cur = cur.next
#
#         return dumy.next
#

# 解法2

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dumy = ListNode(0)
        dumy.next = head
        prev = dumy
        cur = head  # 记住定义，看一下当前元素的重复值
        while cur:  # 迭代就是迭代每一个元素 而cur的定义要清楚
            curRepeatNum = 0
            difNode = cur  # 这里初始化 你要是difNode=head就错了兄弟
            while difNode and difNode.val == cur.val:
                curRepeatNum += 1
                difNode = difNode.next
            if curRepeatNum > 1:
                prev.next = difNode
            else:
                prev = cur
            cur = difNode

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
    nums = [1, 1, 1, 2, 3]
    head = create_linked_list(nums)
    solution = Solution()
    result = solution.deleteDuplicates(head)
    print(print_linked_list(result))
