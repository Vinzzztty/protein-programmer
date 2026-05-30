from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        current = head

        while current:
            if current in seen:
                return True
            seen.add(current)
            current = current.next

        return False


# Test
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # pos = 1 (balik ke node2)

sol = Solution()
print(sol.hasCycle(node1))  # True
