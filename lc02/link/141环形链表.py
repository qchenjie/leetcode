# 判断有没有环


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        fast = head.next   # 这里设置fast = head，那下面的大循环第一次就不成立了
        slow = head
        while fast != slow:
            if not fast or not fast.next:
                return False
            fast  = fast.next.next
            slow = slow.next
        return True


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
    head = create_linked_list(nums)
    solution = Solution()
    result = solution.hasCycle(head)
    print(result)
