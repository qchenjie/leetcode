class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k: int):
        if not head or not head.next or k == 0:
            return head
        # 计算链表的长度
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        # 如果反转整数倍的链表长度，直接返回
        # if n % k == 0:
        #     return head
        # 减少计算量
        if k % n == 0:
            return head
        else:
            k = k % n  # 当大于链表的长度的时候，旋转k还是旋转它的模都是一样的

        # 先反转整体
        rehead = self.reverse(head)

        # 找到k个位置
        cur = rehead
        while k - 1:
            cur = cur.next
            k -= 1
        # 保存后面的
        secondhead = cur.next
        # 断开
        cur.next = None

        # 反转前面的
        newhead = self.reverse(rehead)

        # 反转后面的
        secondhead = self.reverse(secondhead)

        # 连起来
        rehead.next = secondhead

        return newhead

    def reverse(self, head):
        if not head:
            return
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev


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
    head = [1, 2]
    k = 2
    head = create_linked_list(head)
    solution = Solution()
    result = solution.rotateRight(head,k)
    print(print_linked_list(result))
