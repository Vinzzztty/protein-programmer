# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # using two pointers
        fast = head
        slow = head

        # Debugging output awal
        print(f"Starting list: {head}")
        print(f"Removing {n}th node from the end")

        # Geser pointer fast sejauh n langkah
        for _ in range(n):
            fast = fast.next
            print(f"Fast pointer moved to: {fast}")

        # Jika fast sudah mencapai akhir, berarti elemen yang dihapus adalah yang pertama
        if not fast:
            print("Fast pointer reached the end, removing the head")
            return head.next

        # Pindahkan fast ke akhir, sambil memindahkan slow satu per satu
        while fast.next:
            fast = fast.next
            slow = slow.next
            print(f"Fast pointer: {fast}, Slow pointer: {slow}")

        # Debugging sebelum menghapus elemen
        print(f"Node to remove: {slow.next}")

        # Hapus node ke-n dari akhir
        slow.next = slow.next.next

        # Debugging setelah penghapusan
        print(f"List after removal: {head}")

        return head


# Fungsi bantu untuk membuat linked list dari daftar
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# Contoh penggunaan:
list1 = create_linked_list([1, 2, 3, 4, 5])

solution = Solution()
result = solution.removeNthFromEnd(head=list1, n=2)
print(result)
