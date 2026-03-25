class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_dupes(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head
    while curr and curr.next:
        if curr.value == curr.next.value:
            while curr.value == curr.next.value:
                curr = curr.next
            curr = curr.next
            prev.next = curr
        else:
            prev = prev.next
            curr = curr.next
    return dummy.next


head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))
head2 = Node(1, Node(1, Node(1, Node(2, Node(2, Node(3))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))
print_linked_list(delete_dupes(head2))