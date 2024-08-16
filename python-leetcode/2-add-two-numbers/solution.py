# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Inisialisasi head to store answer and current keep tracking node
        head = ListNode()
        carry = 0
        current = head

        # Perhitungan linked list
        while l1 != None or l2 != None or carry != 0:
            # GET l1 value
            l1_value = l1.val if l1 else 0

            l2_value = l2.val if l2 else 0

            total = l1_value + l2_value + carry

            # Debugging output untuk melihat setiap langkah perhitungan
            print(
                f"l1_value: {l1_value}, l2_value: {l2_value}, carry: {carry}, total: {total}"
            )

            # Move to next node
            current.next = ListNode(total % 10)  # total % 10 untuk mencari angka sisa

            carry = total // 10  # angka yang disimpan atau lebih dari 10

            # Move to next value for l1, and l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            current = current.next

            # Debugging output untuk melihat status linked list sementara
            print(f"Current linked list: {head.next}")

        return head.next


# Fungsi bantu untuk membuat linked list dari daftar
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# Contoh penggunaan:
list1 = create_linked_list([2, 4, 3])
list2 = create_linked_list([5, 6, 4])

solution = Solution()
result = solution.addTwoNumbers(list1, list2)
print(result)
