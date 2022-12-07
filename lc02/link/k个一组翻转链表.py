# 判断有没有环


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        dumy = ListNode(0, head)

        # 计算链表的长度
        cur = head
        len_head = 0
        while cur:
            cur = cur.next
            len_head += 1

        # 计算次数
        n = len_head // k

        # 初始化
        # prev的位置
        prev = dumy
        # 找到last位置
        last = head
        k_temp = k
        while k_temp - 1:
            last = last.next
            k_temp -= 1
        # 找到next的位置
        next = last.next

        while n:
            k_temp = k
            last.next = None
            prev.next = None  # 断开

            # 开始反转
            temp = self.reverse(head)

            # 反转完成了开始连接
            prev.next = temp
            head.next = next

            # 开始更新
            prev = head
            head = next
            last = next
            n -= 1
            if n:
                while k_temp - 1:
                    last = last.next
                    k_temp -= 1
                next = last.next

        return dumy.next

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


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
    k = 2
    head = create_linked_list(nums)
    solution = Solution()
    result = solution.reverseKGroup(head, k)
    print(print_linked_list(result))
