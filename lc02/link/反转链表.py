# 反转链表

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 法一，用递归的来写

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 这样写，不要误会，这个是和其他代码一样是先判断一下,就是万一一进来就是空的（每一个代码都有）
        if head is None:
            return head

        # 下面这个是 递归的终止条件
        if head.next is None:
            return head  # 这里总是会错

        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        # 终止条件的返回和这个的返回可不是一个东西
        return temp

# # ----------------下面两个 reverseListTest和reverseListchen是我测试用的 -----------------------------------
#
#     def reverseListTest(self, head: ListNode) -> ListNode:
#         chen = head
#         # 找到最后一个节点,先记着
#         while chen.next:
#             chen = chen.next
#         self.reverseListchen(head)
#         return chen
#
#
#     def reverseListchen(self, head:ListNode) :
#         # 这样写，不要误会，这个是和其他代码一样是先判断一下,就是万一一进来就是空的（每一个代码都有）
#         if head is None:
#             return
#
#             # 下面这个是 递归的终止条件
#         if head.next is None:
#             return
#
#         self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#


# 法二
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head:
#             return None
#         pre=None
#         cur=head
#         while cur:
#             nextnode = cur.next
#             cur.next = pre
#             pre = cur
#             cur = nextnode  # cur = cur.next (常见的错误)
#         return pre


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
    nums = [1, 2, 3, 4, 5, 6]
    head = create_linked_list(nums)
    solution = Solution()
    result = solution.reverseList(head)
    print(print_linked_list(result))
    # print(result)
