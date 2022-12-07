from typing import List

l1 = [4, 2, 1]
l2 = [4, 3, 1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        l1 = self.reverseList(l1)
        l2 =self.reverseList(l2)

        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next

    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pre = None
        cur = head
        while cur.next:
            head = cur.next
            cur.next = pre
            pre = cur
            cur = head
        head.next = pre
        return head


if __name__ == '__main__':
    chen = Solution()
    print(chen.mergeTwoLists(l1, l2))
