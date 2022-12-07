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
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or head.next:
            return head
        dumy = ListNode(0, head)
        # 维护两个指针，lastsord表示已维护好的指针的最后一个指针，cur表示当前的指针
        lastsord = head
        cur = head.next
        while cur:
            # 如果当前值小于已维护好的最后一个指针
            if cur.val >= lastsord.val:
                lastsord = cur
                cur = cur.next
            # 否则的话就，从虚拟节点开始找位置(也就是第一个大于cur的位置)
            else:
                pre = dumy
                # 之前的问题，看next的值的时候先判断next在不在
                while pre.next and pre.next.val < cur.val:
                    pre = pre.next
                # 找好之后开始插入
                # 下面的就是开始插入逻辑，没什么好看的
                lastsord.next = cur.next  # 每一次总会在某一些小地方出错
                cur.next = pre.next
                pre.next = cur

                # 循环下一个要处理的，（lastsord是已处理好的部分）
                cur = lastsord.next  # 这里我刚开始写成了cur=cur.next

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
    nums = [-1, 5, 3, 4, 10]
    head = create_linked_list(nums)
    solution = Solution()
    result = solution.insertionSortList(head)
    print(print_linked_list(result))
    # print(result)
