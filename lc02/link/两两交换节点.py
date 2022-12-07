# 简单的删除链表的元素

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 递归终止条件
        if not head or not head.next:
            return head
        newHead = head.next
        # 先递进去,下面再归出来，就像一直root.left,下面这句拆开来写
        # head.next = self.swapPairs(newHead.next)
        temp=self.swapPairs(newHead.next)
        # 本层要的是,这就是之前的反转链表
        head.next=temp
        newHead.next = head

        return newHead


# 我放弃递归了兄弟
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         dumy=ListNode(0,head)
#         pre=dumy
#         node1=head
#         while node1 and node1.next:
#             node2 = node1.next
#             node1.next=node2.next
#             node2.next=node1
#             pre.next=node2
#         return dumy.next

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
    result = solution.swapPairs(head)
    print(print_linked_list(result))
