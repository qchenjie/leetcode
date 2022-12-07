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
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        small = ListNode(-1)
        big = ListNode(-1)

        pro = head  # 迭代每一个head

        smallHead = small  # 用来下面作为.next用的
        bigHead = big

        while pro:
            if pro.val >= x:
                bigHead.next = pro
                bigHead = bigHead.next
            else:
                smallHead.next = pro
                smallHead = smallHead.next
            prp = pro.next

        # 这里是个细节，整个题目就是这里导致是中等的
        bigHead.next = None
        # 合一下
        smallHead.next = big.next
        return small.next


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
    nums = [1, 4, 3, 2, 5, 2]
    head = create_linked_list(nums)
    solution = Solution()
    result = solution.partition(head,2)
    print(print_linked_list(result))
    # print(result)
