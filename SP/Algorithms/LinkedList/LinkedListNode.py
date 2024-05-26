class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"|data={self.data}| next->{repr(self.next)}"



class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def push_ll(self, new_data):
        new_node = Node(data=new_data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def append_ll(self, new_data):
        new_node = Node(data=new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_ll(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    def reverse_ll(self):
        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    def find_cycle(self):
        if not self.head:
            return False

        fast = self.head
        slow = self.head

        while fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def create_cycle(self, pos):
        if pos < 0 or not self.head:
            return  # Invalid position or empty list

        last = self.head
        end = None
        index = 0

        # Find the node at the specified position
        while last.next:
            if index == pos:
                end = last
            last = last.next
            index += 1

        # Make the last node point to the node at the specified position
        if end:
            last.next = end


def merge_two_sorted_lists(l1, l2):
        dummy = Node()
        tail = dummy
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return dummy.next





if __name__ == "__main__":
    ll = LinkedList()

    for i in range(2, 21):
        ll.append_ll(i)
    ll.print_ll()
    ll.push_ll(1)
    ll.push_ll(3)
    ll.print_ll()
    print(f"\n Is there a cycle in the list? {ll.find_cycle()}")
    ll.reverse_ll()
    ll.print_ll()
    ll.create_cycle(3)
    print(f"\n Is there a cycle in the list? {ll.find_cycle()}")

    l1 = Node(1, Node(3, Node(5, Node(6))))
    l2 = Node(2, Node(4, Node(7)))
    while l1:
        print(l1.data, end="->")
        l1 = l1.next
    print("None")

    l3 = LinkedList()
    l4 = LinkedList()
    data_3 = [10, 20, 30, 40, 50, 666]
    data_4 = [15, 25, 30, 45, 50, 666]

    for i in data_3:
        l3.append_ll(i)
    for i in data_4:
        l4.append_ll(i)

    # Example usage
    list1 = Node(1, Node(3, Node(5)))
    list2 = Node(2, Node(4, Node(6)))

    print(repr(list1))
    print(repr(list2))
    merged_list = merge_two_sorted_lists(list1, list2)

    print(repr(merged_list))

    while merged_list:
        print(merged_list.data, end=" -> ")
        merged_list = merged_list.next
    # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 ->








