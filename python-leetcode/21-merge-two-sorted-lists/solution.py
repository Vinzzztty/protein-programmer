# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # inisialisasi head
        head = ListNode()
        print(f"Head node initialized: {head.val}")

        # inisialisasi pointer
        current = head

        # Looping untuk membandingkan nilai masing masing list node
        while list1 and list2:
            print(f"Comparing list1.val: {list1.val} with list2.val: {list2.val}")
            if list1.val < list2.val:
                current.next = list1
                print(f"Attaching list1 node with value: {list1.val} to merged list.")
                list1 = list1.next

            else:
                current.next = list2
                print(f"Attaching list2 node with value: {list2.val} to merged list.")
                list2 = list2.next

            current = current.next
            print(f"Moved to next node in merged list: {current.val}")

        if list1 != None:
            current.next = list1
            print(f"Attaching remaining nodes from list1 starting with: {list1.val}")

        else:
            current.next = list2
            print(f"Attaching remaining nodes from list2 starting with: {list2.val}")

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
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

solution = Solution()
result = solution.mergeTwoLists(list1, list2)
print(f"Merged List: {result}")
